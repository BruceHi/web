from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])  # put 的本质实现还是 deque.append()，所以放入里面的是一个整体。


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    # p.join()
