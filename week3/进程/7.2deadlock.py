# 死锁
from multiprocessing import Process, Queue


# def f(q):
#     q.put('X' * 1000000)  # 缓存太多，不及时取出数据，就会造成阻塞等待消耗。

def f(q):
    q.put('X')  # 不会造成死锁


if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    p.join()
    obj = queue.get()
    print(obj)

    # join 是等待子进程结束，此时子进程是关闭状态。
    # 死锁，去掉这一句 或 与后面一句对调位置。
