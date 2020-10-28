from multiprocessing import Process, Lock, Value
import time


def job(v, num, l):
    l.acquire()
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print(v.value, end='|')
    l.release()


if __name__ == '__main__':
    l = Lock()
    v = Value('i', 0)
    p1 = Process(target=job, args=(v, 1, l))
    p2 = Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
