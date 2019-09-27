'''
破解有道词典
V18
'''

from urllib import request, parse


def youdao(key):

    url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {
        "i": key,
        "from":"AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1523100789519",
        "sign": "b8a55a436686cd89873fa46514ccedbe",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult": "false"
    }

    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
                    "Accept" : "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding" : "gzip, deflate",
                    "Accept-Language" : "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
                    "Connection" : "keep-alive",
                    "Content-Length" : "240",
                    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
                    #"Cookie" : "OUTFOX_SEARCH_USER_ID=-663731727@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=347942893.56518316; P_INFO=he.x.m123@163.com|1566436782|0|other|11&20|bej&1566211507&study#gud&441200#10#0#0|150467&0|study_client&study|he.x.m123@163.com; JSESSIONID=aaaYe2k-dz9lP4SHxUW1w; ___rl__test__cookies=1569563069746",
                    "Host" : "fanyi.youdao.com",
                    "Origin" : "http://fanyi.youdao.com",
                    "Referer" : "http://fanyi.youdao.com/",
                    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
                    "X-Requested-With" : "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("boy")