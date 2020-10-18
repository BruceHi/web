from threading import Thread
import time


def start():
    time.sleep(5)


thread1 = Thread(target=start)
print(thread1.is_alive())

thread1.start()

print(thread1.getName())
print(thread1.is_alive())

thread1.join()
print(thread1.is_alive())


