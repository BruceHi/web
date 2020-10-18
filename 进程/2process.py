from multiprocessing import Process


def f(name):
    print(f'hello {name}')


if __name__ == '__main__':
    p = Process(target=f, args=('join',))  # args 的参数必须是元组类型
    p.start()  # 通过创建一个 Process 对象然后调用它的 start() 方法来生成进程
    p.join()  # 等待子进程终止

