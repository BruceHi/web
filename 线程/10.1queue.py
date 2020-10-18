import queue
q = queue.Queue(5)  # 里面省略的话，是无穷大的意思。
q.put(111)
q.put(222)
q.put(333)

print(q.get())
print(q.get())
q.task_done()
print(q.qsize())  # 队列
print(q.empty())
print(q.full())


print('-' * 20)
# 生产者消费者模式
from threading import Thread, Lock, Condition
import random
import time

writelock = Lock()


class Producer(Thread):
    def __init__(self, q, con, name):
        super().__init__()
        self.q = q
        self.con = con
        self.name = name
        print(f'Producer {self.name} Started')

    def run(self) -> None:
        while 1:  # 能一直循环下去。
            # global writelock
            self.con.acquire()

            if self.q.full():
                # with writelock:
                print('Queue is full, please wait.')
                self.con.wait()
            else:
                val = random.randint(0, 10)
                # with writelock:
                print(f'{self.name} put value {str(val)} in queue.')
                self.q.put(f'{self.name}: {str(val)}')
                self.con.notify()
                # self.con.wait() 轮流开始容易造成死锁。
                time.sleep(1)
        # self.con.release()


class Consumer(Thread):
    def __init__(self, q, con, name):
        super().__init__()
        self.q = q
        self.con = con
        self.name = name
        print(f'Consumer {self.name} Started')

    def run(self) -> None:
        while 1:
            # global writelock
            self.con.acquire()

            if self.q.empty():
                # with writelock:
                print('Queue is empty, please wait.')
                self.con.wait()
            else:
                val = self.q.get()
                # with writelock:
                print(f'{self.name} get value {val} from queue.')
                self.con.notify()
                # self.con.wait()  # 这样就是轮流开始了。只是消费得慢一些。这样容易造成死锁。
                time.sleep(1)
        # self.con.release()


if __name__ == '__main__':
    q = queue.Queue(5)
    con = Condition()

    p1 = Producer(q, con, 'p1')
    p1.start()
    p2 = Producer(q, con, 'p2')
    p2.start()
    c1 = Consumer(q, con, 'C1')
    c1.start()










