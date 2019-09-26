from urllib import request, parse
from http import cookiejar

#  创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''

    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"

    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        "email": "he.x.m123@163.com",
        "password": "356126155165352"
    }

    # 把数据进行编码
    data = parse.urlencode(data)
    print(type(data))

    headers = {}
    # headers['User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    #req = request.Request( url, headers=headers)
    # 创建一个请求对象
    req = request.Request(url, headers=headers, data=data.encode())
    print(req)
    #rsp = request.urlopen(req)
    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/965187997/profile"

    # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
    # req = request.Request(url)
    rsp = opener.open(url)

    try:
        html = rsp.read().decode()
        print(html)
        with open("rsp.html", "w", encoding='utf-8') as f:
            f.write(html)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    login()
    getHomePage()