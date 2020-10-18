import time
from multiprocessing import Process


def run():
    print('子进程开启')
    time.sleep(2)
    print('子进程结束')


if __name__ == '__main__':
    print('父进程开启')
    p = Process(target=run)
    p.start()
    # p.join()  # 有这一句，父进程要等子进程结束后才能继续运行，没有的话，谁运行的快，谁结束
    print('父进程结束')
