import os
import time
from multiprocessing import Process


class NewProcess(Process):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self) -> None:
        while True:
            print(f'我是进程 {self.num}，我的 id 是：{os.getpid()}')
            time.sleep(1)


if __name__ == '__main__':  # 多进程需要在main函数中运行，否则报错，所以该句不可省略。
    for i in range(2):
        p = NewProcess(i)
        p.start()  # 其实调用的是 run 方法，所以 run 方法要重写。
