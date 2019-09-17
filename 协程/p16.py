# 案例16
from concurrent.futures import ThreadPoolExecutor as Pool
#import requests
import urllib
from urllib import request

URLS = ['http://www.baidu.com', 'http://www.qq.com', 'http://sina.com.cn']


def task(url, timeout=20):
    #return requests.get(url, timeout=timeout)
    return request.urlopen(url, timeout=timeout)


pool = Pool(max_workers=3)
results = pool.map(task, URLS)

import time
time.sleep(1)
for ret in results:
    print('%s, %s' % (ret.url, len(ret.read())))