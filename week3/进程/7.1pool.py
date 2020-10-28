# 进程池
from multiprocessing import cpu_count
from multiprocessing.pool import Pool
from time import sleep, time
import random
import os


def run(name):
    print('%s子进程开始，进程ID: %d' % (name, os.getpid()))
    start = time()
    sleep(random.choice([1, 2, 3, 4]))
    end = time()
    print('%s子进程结束，进程ID: %d。耗时 %.2f s' % (name, os.getpid(), end-start))


if __name__ == '__main__':
    print('父进程开始')
    p = Pool(cpu_count())
    for i in range(10):
        p.apply_async(func=run, args=(i,))
    p.close()
    p.join()  # 必须要有 close，或 terminate 否则报错 AssertionError。若是 terminate，则不执行子进程了。
    print('父进程结束')
    # p.terminate()
