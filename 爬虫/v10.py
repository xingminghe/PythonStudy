'''
使用代理访问百度网站
'''

from urllib import  request, error

if __name__ == '__main__':

    url = "https://www.baidu.com"

    # 使用代理步骤
    # 1. 设置代理地址
    proxy = {'http': '1.197.204.247:9999'}
    # 2. 创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3. 创建Opener
    opener = request.build_opener(proxy_handler)
    # 4. 安装Opener
    request.install_opener( opener)

    # 现在如果访问url，则使用代理服务器
    try:

        #req = request.Request(url)
        #req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36")
        rsp = request.urlopen(url)

        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)