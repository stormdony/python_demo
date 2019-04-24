# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 13:48
# @Author  : donlex
# @Email   : donlex@qq.com
# @Software: PyCharm 2018.1.4 (Professional Edition)
from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
def scan_login(url):
    driver.get(url)
    # 等待扫码登录
    sleep(15)
    # 进入之后开始其他操作

if __name__ == '__main__':
    url = 'https://login.taobao.com/member/login.jhtml'
    scan_login(url)