from multiprocessing import Process, Value
import time


def job(v, num):
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print(v.value, end='|')


if __name__ == '__main__':
    v = Value('i', 0)
    p1 = Process(target=job, args=(v, 1))
    p2 = Process(target=job, args=(v, 3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

