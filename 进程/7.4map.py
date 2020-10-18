# map 函数的并行版本
from multiprocessing.pool import Pool
import time
from random import choice
import os

def f(x):
    start = time.time()
    # time.sleep(choice([1, 2, 3, 4, 5]))
    time.sleep(1)
    end = time.time()
    return x, os.getpid(), os.getppid()

def run(name):
    print('%s子进程开始，进程ID: %d' % (name, os.getpid()))
    start = time.time()
    time.sleep(choice([1, 2, 3, 4]))
    end = time.time()
    print('%s子进程结束，进程ID: %d。耗时 %.2f s' % (name, os.getpid(), end-start))
    return name


if __name__ == '__main__':
    with Pool(processes=6) as pool:
        # 只支持一个参数，并且返回结果是列表。待所有结束后，才返回结果。
        # 下面创建了 10 个进程，每个进程的开始和结束时间并不相同。但返回结果还是顺序返回的。
        # 进程的 Pool.map 和 普通的 map 返回结果相同，但耗时差距巨大。

        start = time.time()
        print(pool.map(f, range(10)))  # 10 个进程并行
        end = time.time()
        print('耗时时间：', end-start)
        #
        # print('----------')
        # start = time.time()
        # print(list(map(f, range(10))))  # 同一个进程
        # end = time.time()
        # print('耗时时间：', end-start)

        it = pool.imap(f, range(10))
        print(it)
        print(next(it))
        print(next(it))
        print(it.next(timeout=1))  # next 为 pool.IMapIterator 的方法
