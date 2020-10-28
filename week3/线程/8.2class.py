# 继承多线程
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self) -> None:
        time.sleep(2)
        print('current task：', self.n)


if __name__ == '__main__':
    print('主线程开始')
    t1 = MyThread('thread 1')
    t2 = MyThread('thread 2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('主线程结束')
