from concurrent.futures import ThreadPoolExecutor
import time


def func(args):
    print(f'call func {args}')


if __name__ == '__main__':
    seed = ['a', 'b', 'c', 'd']

    with ThreadPoolExecutor(3) as executor:
        executor.submit(func, seed)  # submit 将 seed 当成一个整体

    time.sleep(1)

    with ThreadPoolExecutor(3) as executor:
        executor.map(func, seed)  # 当成一个一个元素执行。立即执行，func 是异步执行的，对 func 的多个调用可以并发执行。

    time.sleep(1)

    with ThreadPoolExecutor(1) as executor:
        future = executor.submit(pow, 2, 3)  # 返回 future 对象。
        print(future.result())  # 返回调用返回的值。
