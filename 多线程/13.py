import threading
import time

# python2
# from Queue import Queue

#Python3
import queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # qsize返回queue内容长度
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = "生成产品" + str(count) + "##"
                    #put是往queue中放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(1)
            if queue.qsize() > 700:
                break


class Consumer(threading.Thread):
    def run(self):
        global  queue
        while True:
            if queue.qsize() > 100:
                for i in range(100):
                    # get是从queue中取出一个值
                    msg = self.name + "消费了" + queue.get() + "**"
                    print(msg)
            time.sleep(0.5)


if __name__ == "__main__":
    queue = queue.Queue()
    print(queue.qsize())

    for i in range(500):
        msg = "初始产品" + str(i) + "@@"
        queue.put(msg)
        print(msg)
    print(queue.qsize())

    for i in range(3):
        print("第{0}轮产出".format(i+1))
        p = Producer()
        p.start()
    for i in range(8):
        print("第{0}轮消费".format(i+1))
        c = Consumer()
        c.start()
