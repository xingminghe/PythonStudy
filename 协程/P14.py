# 案例14
from concurrent.futures import ThreadPoolExecutor
import time


def return_future(msg):
    time.sleep(3)
    return msg


# 创建一个线程池
pool = ThreadPoolExecutor(max_workers=4)

# 往线程池加入2个task
f1 = pool.submit(return_future, 'hello')
f2 = pool.submit(return_future, 'world')
f3 = pool.submit(return_future,"Nihao")
f4 = pool.submit(return_future,"I am fine")

print(f1.done())
print(f2.done())
time.sleep(3.1)
print(f3.done())
print(f4.done())

print(f1.result())
print(f2.result())
print(f3.result())
print(f4.result())