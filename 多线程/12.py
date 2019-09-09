import threading
sum = 0
loopSum = 1000000

lock = threading.Lock()

def myAdd():
    global sum, loopSum
    lock.acquire()
    for i in range(1,loopSum):
        sum += 1
    print("运行myAdd后sum的值现在是{}".format(sum))
    lock.release()

def myMinu():
    global sum, loopSum
    lock.acquire()
    for i in range(1,loopSum):
        sum -= 1
    print("运行myMinu后sum的值现在是{}".format(sum))
    lock.release()

if __name__ == '__main__':
    print("Starting......{0}".format(sum))

    #开始多线程实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd)
    t2 = threading.Thread(target=myMinu)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done.......{0}".format(sum))
