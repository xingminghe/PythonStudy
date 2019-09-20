# -*- coding: utf-8 -*-

import sys
import ftplib
import re
import os
import argparse
import datetime
from ftplib import FTP
from io import BytesIO
from zipfile import ZipFile

ftp = FTP("10.74.15.155")
ftp.login("mcfuse", "mcfuse")


def filterlog(logpath, datefrom, dateto):
    try:
        ftp.cwd(logpath)
        filelist = ftp.nlst()
    except ftplib.error_perm:
        return

    pa = re.compile(r'^(?P<Pid>[A-Z0-9]{16})_(?P<Station>[A-Z][A-Z2]{0,4}.)(?P<DateTime>201\d{11})\d\d.*\.zip')

    for log in filelist:
        ma = pa.match(log)
        if ma:
            dt = datetime.datetime.strptime(ma.group('DateTime'), "%Y%m%d%H%M%S")
            if datefrom <= dt <= dateto:
                yield log


def copylog(logpath, logfiles, destination):
    ftp.cwd(logpath)
    os.chdir(destination)

    for log in logfiles:
        ftp.retrbinary('RETR ' + log, open(log, 'wb').write)
        print(log)

    return


def unziplog(logpath, logfiles, destination):
    ftp.cwd(logpath)
    os.chdir(destination)

    for log in logfiles:
        myfile = BytesIO()

        def handle_binary(more_data):
            myfile.write(more_data)

        ftp.retrbinary('RETR ' + log, handle_binary)

        with ZipFile(myfile, "r") as zip_ref:
            zip_ref.extractall(destination)

        print(log)

    return


def duration(starttime, endtime):
    if starttime:
        start = makeuptime(starttime)
    else:
        t = datetime.datetime.now()
        start = datetime.datetime(t.year, t.month, t.day)

    if endtime:
        end = makeuptime(endtime)
    else:
        end = datetime.datetime.now()

    if start > end:
        print("error: start time (%s) later than end time (%s)" % (
        starttime.strftime("%Y%m%d%H%M"), endtime.strftime("%Y%m%d%H%M")))
        sys.exit()

    days = []
    day = datetime.datetime(start.year, start.month, start.day)
    while True:
        days.append(day.strftime("%Y%m%d"))
        day += datetime.timedelta(days=1)
        if day > end:
            break

    return {'start': start, 'end': end, 'days': days}


def makeuptime(timestr):
    l = 12 - len(timestr)
    if 0 <= l <= 12:
        try:
            return
        except ValueError:
            print("error to use %s as datetime" % timestr)
            sys.exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Query, download and unzip PtisPlus log files from ftp server')
    parser.add_argument('station', metavar='station_name', help="Station name like BB1, CAL, RFT...")
    parser.add_argument('-p', '--program', metavar='program_name', choices=['FRT', 'ES2', 'CO2','MP2'], default='FRT',
                        help="Program name like FRT, ES2, CO2")
    parser.add_argument('-f', '--start', metavar='YYYYMMMDDHHMM', default='',
                        help="Start date time, in format 'YYYYMMDDHHMM; today 00:00 if empty")
    parser.add_argument('-t', '--end', metavar='YYYYMMMDDHHMM', default='',
                        help="End date time, in format 'YYYYMMDDHHMM; now if empty")
    parser.add_argument('-s', '--status', metavar='PASSED', choices=['PASSED', 'FAILED', 'Both'], default='PASSED',
                        help="PASSED, or FAILED, or Both; PASSED if empty")
    parser.add_argument('-m', '--mode', metavar='OPE', choices=['OPE', 'ENG', 'Both'], default='OPE',
                        help="OPE, or ENG, or Both; OPE if empty")
    parser.add_argument('--allforms', action='store_true',
                        help="All standardforms like StandardForm0, 1, 2, 3; StandardForm0 if empty")
    parser.add_argument('--onlycopy', action='store_true', help="Copy but not unzip; Copy and unzip if empty")
    parser.add_argument('--copyto', metavar='target_folder', default='',
                        help="Folder to copy the files to, to current folder if empty")

    args = parser.parse_args()

    # du: duration
    du = duration(args.start, args.end)

    # om: operation mode
    if args.mode == 'Both':
        om = ('OPE', 'ENG')
    else:
        om = (args.mode,)

    # ss: station_status
    if args.status == 'Both':
        ss = (args.station + 'PASSED', args.station + 'FAILED')
    else:
        ss = (args.station + args.status,)

    # sf: standardform
    if args.allforms:
        sf = ('StandardForm0', 'StandardForm1', 'StandardForm2', 'StandardForm3')
    else:
        sf = ('StandardForm0',)

    # (r"/LOG/FRT/20171204/StandardForm0/OPE/ANTPASSED/"
    allfolders = ("/MC-Log/%s/%s/%s/%s/%s/" % (args.program, d, f, o, s) for d in du['days'] for f in sf for o in om for s
                  in ss)

    qty = 0
    folder_files = {}
    for folder in allfolders:
        print(folder)
        folder_files[folder] = []
        for log in filterlog(folder, du['start'], du['end']):
            qty += 1
            folder_files[folder].append(log)
            print('\t' + log)

    if qty == 0:
        print("No log files.")
    else:
        if args.copyto:
            destination = args.copyto
        else:
            destination = os.getcwd()

        if args.onlycopy:
            print("Total %s log files, copy to %s? y/n?" % (qty, destination))
        else:
            print("Total %s log files, copy and unzip to %s? y/n?" % (qty, destination))

        answer = input()
        if answer == 'y':
            try:
                os.mkdir(destination)
            except FileExistsError:
                pass

            if args.onlycopy:
                for folder in folder_files:
                    if folder_files[folder]:
                        copylog(folder, folder_files[folder], destination)
            else:
                for folder in folder_files:
                    if folder_files[folder]:
                        unziplog(folder, folder_files[folder], destination)

            print('done')