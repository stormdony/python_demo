# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 13:50
# @Author  : donlex
# @Email   : donlex@qq.com
# @Software: PyCharm 2018.1.4 (Professional Edition)

import requests
import json

import time
import random
from wordcloud import WordCloud
import jieba
from matplotlib import pyplot as plt

from pyecharts import Bar, Pie


class MaoYan(object):

    def __init__(self, url, header):
        self.url = url
        self.header = header

    def get_comments(self):
        '''
        爬取评论信息
        :return:
        '''
        for i in range(0, 14352, 15):
            URL = self.url.format(i)
            data = requests.get(url=URL, headers=self.header)
            time.sleep(random.random() * 3)
            com = json.loads(data.text)
            comments = com['data']['comments']
            if comments:
                for item in comments:
                    data = {
                        'content': item['content'],
                        'score': item['score'],
                        'nick': item['nick'],
                        'gender': item['gender'],
                    }
                    print(data)
                    # 存入文本中
                    with open('comments.txt', 'a+', encoding='UTF-8') as file:
                        file.writelines(
                            json.dumps(data, ensure_ascii=False) + '\n')
            else:
                break

    def readFile(self):
        '''
        读取评论信息文件
        :return:
        '''
        with open('comments.txt', 'r+', encoding='UTF-8') as file:
            lists = file.readlines()
        return lists

    def get_context(self):
        '''获取并拼接所有的评论'''
        lists = self.readFile()
        text = ""
        for item in lists:
            line = json.loads(item)
            content = line['content']
            text += content
        return text

    def get_wordcloud(self):
        '''
        制作词云图
        :return:
        '''
        text = self.get_context()
        seg_list = jieba.cut(text, cut_all=True)
        wc = WordCloud(background_color="#CCC",  # 设置背景颜色
                       # mask = pic , #设置背景图片
                       max_words=2000,  # 设置最大显示的字数
                       margin=5,
                       font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",  # 不加这一句显示口字形乱码
                       max_font_size=80,  # 设置字体最大值
                       random_state=40,  # 设置有多少种随机生成状态，即有多少种配色方案
                       )
        w1 = "/ ".join(seg_list)  # 全模式
        mword = wc.generate(w1)
        plt.imshow(mword)
        plt.axis("off")
        plt.savefig('wordcloud.png')  # 保存图片
        plt.show()

    def get_single_attribute(self, word):
        '''
        根据传入的属性，返回相应的字典，便于使用pyecharts
        :param word: 属性值
        :return: dict
        '''
        lists = self.readFile()
        list = []
        for line in lists:
            item = json.loads(line)
            list.append(item[word])
        list_to_set = set(list)
        dict = {}
        for gender in list_to_set:
            dict[gender] = list.count(gender)
        return dict

    def draw_score_bar(self):
        bar = Bar('评分柱状图', '来自:猫眼电影')
        data = self.get_single_attribute('score')
        bar.add('分数',
                list(data.keys()),
                list(data.values()),
                is_more_utils=True  # 设置最右侧工具栏
                )
        bar.render('./score.html')

    def draw_gender_Pie(self):
        data = self.get_single_attribute('gender')
        attr = list(data.keys())
        v1 = list(data.values())
        pie = Pie('性别环形图', title_pos='center')
        pie.add(
            '', attr, v1,  # ''：图例名（不使用图例）
            radius=[40, 75],  # 环形内外圆的半径
            is_label_show=True,  # 是否显示标签
            label_text_color=None,  # 标签颜色
            legend_orient='vertical',  # 图例垂直
            legend_pos='left'
        )
        pie.render('./gender.html')

    def crawel(self):
        self.get_comments()
        self.get_wordcloud()
        self.draw_score_bar()
        self.draw_gender_Pie()


if __name__ == '__main__':
    url = 'http://m.maoyan.com/review/v2/comments.json?movieId=410629&userId=-1&offset={}&limit=15&ts=1550987272364&type=3'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Connection': 'keep - alive'}
    spyder = MaoYan(url, header)
    spyder.crawel()
