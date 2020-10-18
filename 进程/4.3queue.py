from multiprocessing import Process, Queue
import os
import time


def write(q):
    print(f'启动 write 子进程：{os.getpid()}')
    for i in 'ABCD':
        q.put(i)
        time.sleep(1)
    print(f'结束 write 子进程：{os.getpid()}')


def read(q):
    print(f'启动 Read 子进程：{os.getpid()}')
    while True:
        val = q.get()
        print(val)
    print(f'结束 Read 子进程：{os.getpid()}')


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()

    pw.join()
    pr.terminate()
    print(f'父进程结束：{os.getpid()}')




