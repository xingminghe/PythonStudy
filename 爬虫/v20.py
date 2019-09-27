'''
爬去豆瓣电影数据
了解ajax的基本爬去方式

'''
from urllib import request
import json


url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"


rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)
f = open("123.txt",'r+',encoding='utf-8')
f.truncate()
for item in data:
    print("{0}:{1}".format(item['title'],item['url']))
    f.write("{0}:{1}\n".format(item['title'],item['url']))
    #print(item['url'])
f.close()
