'''
通过webdriver操作进行查找
'''

from selenium import webdriver
import time

# 通过Keys模拟键盘
from selenium.webdriver.common.keys import  Keys

# 操作哪个浏览器就对哪个浏览器建一个实例
# 自动按照环境变量查找相应的浏览器
driver = webdriver.Chrome(executable_path=r"C:\Users\H0136582\Downloads\chromedriver_win32\chromedriver")

# 如果浏览器没有在相应环境变量中，需要指定浏览器位置

driver.get("http://www.baidu.com")

# 通过函数查找title标签
print("Title: {0}".format(driver.title))