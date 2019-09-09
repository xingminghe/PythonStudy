import threading
import  time

lock1 = threading.Lock()
lock2 = threading.Lock()

def func_1():
    print("func_1 starting.........")
    lock1.acquire()
    print("func_1 申请了lock1.......")
    time.sleep(2)
    print("func_1 等待lock2.........")
    lock2.acquire()
    print("func_1申请了lock2........")
    lock2.release()
    print("func_1释放了lock2")

    lock1.release()
    print("func_1释放了lock1")


def func_2():
    print("func_2 starting.........")
    lock2.acquire()
    print("func_2 申请了 lock_2....")
    time.sleep(4)
    print("func_2 等待 lock_1.......")
    lock1.acquire()
    print("func_2 申请了 lock_1.......")

    lock1.release()
    print("func_2 释放了 lock_1")

    lock2.release()
    print("func_2 释放了 lock_2")

    print("func_2 done..........")


if __name__ == "__main__":
    print("主程序启动..............")
    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序启动..............")
