from multiprocessing.pool import Pool
import time


def f(x):
    time.sleep(500)
    return x * x


if __name__ == '__main__':
    with Pool(processes=6) as pool:
        res = pool.apply_async(func=f, args=(1,))  # 第一个参数是函数对象
        # print(res.get(timeout=1))
        #
        # res = pool.apply_async(func=time.sleep, args=(2,))
        # print(res.get(timeout=1))
        # pool.join()
    print('hello')
