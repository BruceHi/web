from multiprocessing import Process

num = 100


def run():
    print('子进程开始')
    global num
    num += 1
    print(f'子进程 num：{num}')
    print('子进程结束')


if __name__ == '__main__':
    print('父进程开始')
    p = Process(target=run)
    p.start()
    p.join()
    print(f'父进程结束 num：{num}')
    # 全局变量在多个进程中不能共享
