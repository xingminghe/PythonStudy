import time

def Printtime(func):
    def wapper():
        print('Time is {}'.format(time.ctime()))
        return func()
    return wapper

def Hello():
    print('Hellow world')


Hello()

print('#'*50)
f = Printtime(Hello)
f()