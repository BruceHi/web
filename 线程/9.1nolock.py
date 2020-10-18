from threading import Thread, Lock
import time

num = 0
mutex = Lock()


def addone():
    global num
    # 必须写成 mutex，不能写成 Lock()。
    # 若写成后者，则每次产生一个新地进程就加上自己的锁，而不是全局的锁。这就起不到加锁的目了。
    with mutex:
        num += 1
        time.sleep(1)  # 必须休眠，否则观察不到脏数据
        print(f'num value is {num}')


for i in range(10):
    t = Thread(target=addone)
    t.start()

print('main thread stop')
