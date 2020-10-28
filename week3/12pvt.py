from multiprocessing import Process, Queue
from threading import Thread
import time


def job(q):
    res = 0
    for i in range(10000000):  # 一千万可以拉开差距，1百万使用进程还慢一点。
        res += i + i**2 + i**3
    q.put(res)


# 多进程
def multicore():
    q = Queue()
    p1 = Process(target=job, args=(q,))
    p2 = Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:', res1 + res2)


# 多线程
def multithread():
    q = Queue()  # 多线程也可以使用多进程的 Queue
    t1 = Thread(target=job, args=(q,))
    t2 = Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)


# 普通函数
def normal():
    res = 0
    for _ in range(2):
        for i in range(10000000):
            res += i + i**2 + i**3
    print('normal:', res)


if __name__ == '__main__':
    st = time.time()
    normal()
    s1 = time.time()
    print('normal time: ', s1 - st)
    multithread()
    s2 = time.time()
    print('multithread time: ', s2-s1)
    multicore()
    print('multicore time: ', time.time()-s2)  # 正好是前面的一半
