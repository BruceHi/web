from threading import Thread, Lock
import time
import random

num = 0
mutex = Lock()  # 可以使用上下文管理环境，enter 是加锁，exit 是去掉锁。进程池也可以使用。注意进程地锁不能上下文环境。


class MyThread(Thread):
    def run(self) -> None:
        global num

        # num += 1
        # print(f'{self.name}：num value is {num}')
        # print(num)

        # if mutex.acquire():  # 加锁成功，返回True, 默认 blocking=True 为阻塞使用。
        #     num += 1
        #     print(f'{self.name}：num value is {num}')
        # mutex.release()

        with mutex:
            num += 1
            time.sleep(1)  # sleep 不要放错了，要放在 num 后才能读出藏数据，否则还是先抢占住地先写入。
            print(f'{self.name}：num value is {num}')


for _ in range(10):
    t = MyThread()
    t.start()


