# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 14:23
# @Author  : donlex
# @Email   : donlex@qq.com
# @Software: PyCharm 2018.1.4 (Professional Edition)
import itchat
import requests


def get_response(msg):
    apiUrl = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(
        msg)
    # 发送post请求
    r = requests.post(apiUrl).json()
    # 替换br字符串
    response = r.get('content').replace('{br}', '\n')
    return response

# 用于接收来自朋友间的对话消息
# 如果不用这个，朋友发的消息便不会自动回复


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return get_response(msg['Text'])


if __name__ == '__main__':
    itchat.auto_login(True)
    itchat.run()
