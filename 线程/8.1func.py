# 多线程
from threading import Thread
import os


def f(n):
    print(os.getpid())
    print('current task:', n)


if __name__ == '__main__':
    t1 = Thread(target=f, args=('thread 1',))
    t2 = Thread(target=f, args=('thread 2',))
    t1.start()
    t2.start()

