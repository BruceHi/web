from threading import Thread, Lock, RLock
import time
import random

# Lock 不可以嵌套，否则会产生死锁。
mutex = RLock()


class MyThread(Thread):
    def run(self) -> None:

        with mutex:
            print(f'thread name：{self.name}')
            time.sleep(1)
            mutex.acquire()
            mutex.release()


for _ in range(5):
    t = MyThread()
    t.start()