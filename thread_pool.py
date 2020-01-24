import time
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
import requests

def get_html(url):
    requests.get(url)

urls=[
    'http://google.com',
    'http://yandex.ru',
    'http://mail.ru'
]*30

def calc_something(data):
    a=0
    for i in range(10000):
        a+=i

if __name__=='__main__':
    processPool=ProcessPool(4)
    begin=time.time()
    processPool.map(get_html, urls)
    # processPool.map(calc_something, urls)
    print(time.time()-begin)
    threadPool=ThreadPool(4)
    begin = time.time()
    threadPool.map(get_html, urls)
    # threadPool.map(calc_something, urls)
    print(time.time() - begin)