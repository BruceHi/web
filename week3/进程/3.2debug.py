import os
from multiprocessing import Process
import multiprocessing


def debug_info(title):
    print('-' * 20)
    print(title)
    print('模块名称：', __name__)
    print('父进程：', os.getppid())
    print('当前进程', os.getpid())
    print('-' * 20)


def f(name):
    debug_info('function f')
    print('hello', name)


if __name__ == '__main__':
    debug_info('main')
    p = Process(target=f, args=('bob',))
    p.start()

    # p.join()  #

    # 果然父进程还是要快一些。
    for p in multiprocessing.active_children():  # 当前进程的子进程，返回进程列表。若有 join 等待了，则该句不执行。子进程没有子进程。
        print(f'子进程名称：{p.name}，id：{str(p.pid)}')  # p.name 本质是方法当成属性使用，因为有了 @property 装饰器。
    print('进程结束')
    print(f'cpu核心数量：{str(multiprocessing.cpu_count())}')  # 返回系统的cpu 数量

    # p.join()



