import os
import queue
import requests
from threading import Thread
from fake_useragent import UserAgent


class DownloadThread(Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self) -> None:
        # while True:  # 去掉这一句试一试，好像去掉也没有关系。
        url = self.q.get()
        print(f'{self.name} begin download {url}')
        self.download(url)
        self.q.task_done()
        print(f'{self.name} download complete')

    def download(self, url):
        headers = {'User-Agent': UserAgent().random}
        r = requests.get(url, stream=True, headers=headers)
        file_name = os.path.basename(url) + '.html'
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)


if __name__ == '__main__':
    urls = [
        'https://www.douban.com',
        'https://www.baidu.com',
        'https://cn.bing.com',
    ]

    q = queue.Queue()
    for _ in range(5):
        t = DownloadThread(q)
        t.setDaemon(True)  # 有了这句可以让父线程正常结束运行。主线程结束后，使子线程全部结束退出。
        t.start()  # 没有必要将 run 的开头设置为 true，run 能运行多少次，取决于有多少个 start。
        # t.join() 这样写没有意义，没有线程去抢夺。

    for url in urls:
        q.put(url)

    q.join()  # 阻塞至队列中所有的元素都被接收和处理完毕。
