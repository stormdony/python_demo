# coding: utf-8
'''
猎聘网
'''
import re
import os
import jieba
import logging
import pymongo
import requests
import webbrowser
import collections
from pyecharts import Bar
from bs4 import BeautifulSoup
from functools import partial
from pyecharts import WordCloud
from multiprocessing.pool import Pool



client = pymongo.MongoClient('localhost', 27017)
zhaopin = client['zhaopin']
pywork = zhaopin['pywork']


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Connection': 'keep - alive'
}


def getLink(seachname, pagenum):
    '''
    获取所有岗位的信息
    :param seachname:
    :param pagenum:
    :return:
    '''
    for i in range(pagenum):
        url = "https://www.liepin.com/zhaopin/?init=-1&key={}&curPage={}".format(
            seachname, i)
        web_data = requests.get(url=url, headers=header)
        soup = BeautifulSoup(web_data.content, 'lxml')
        job_list = soup.select(".sojob-list > li")
        for item in job_list:
            name = item.select(".job-info > h3")[0]['title']
            link = item.select(".job-info > h3 > a")[0]['href']
            company = item.select(".company-name > a")[0].text
            salary = item.select(".text-warning")[0].text
            location = item.select(".area")[0].text
            education = item.select(".edu")[0].text
            data = {
                "title": name,
                "link": link,
                "company": company,
                "salary": salary,
                "location": location,
                "education": education,
            }
            pywork.insert_one(data)
            print(data)


def getDetailUrl():
    '''
    获取详细招聘要求的页面链接
    :return:
    '''
    collection_set = pywork.find().limit(500)
    URLList = []
    formerStr = "https://www.liepin.com"
    for item in collection_set:
        if formerStr in item['link']:
            URLList.append(item["link"])
        else:
            URLList.append(formerStr + item["link"])

    print("-" * 20)
    print(len(URLList))
    print("-" * 20)
    return URLList


def getInfo(url, demands_text):
    '''
    提取详细页面的信息
    :param url:
    :param demands_text:
    :return:
    '''
    web_data = requests.get(url, headers=header)
    soup = BeautifulSoup(web_data.content, 'lxml')
    try:
        demands = soup.select(".content-word")[0].contents
        demands = sorted(set(demands), key=demands.index)
        # 删除<br/>
        delete_str = "<br/>"
        br_tag = BeautifulSoup(delete_str, "lxml").br
        demands.remove(br_tag)
        # 拼接所有要求
        for item in demands:
            demands_text += item.replace("\r", "")
        f = open('demands.txt', mode='a+', encoding='UTF-8')
        f.write(demands_text + "\n")
        f.close()
    except:
        logging.warning("warning...")


def CutWordByJieBa(txt, seachname):
    '''
    利用jieba分词提取
    :param txt:
    :param seachname:
    :return:
    '''
    seg_list = jieba.cut(txt, cut_all=True)
    w1 = "/ ".join(seg_list)  # 全模式
    # 提取英文
    fil = re.findall('[a-zA-Z]{1,}/', w1)
    strl = ""
    for i in fil:
        strl += i
    strl = strl.lower()
    result_dic = countfeq(strl)
    showInBar(seachname=seachname, result=result_dic)
    showInWordCount(seachname=seachname, result=result_dic)
    showInBrowser(seachname)


def countfeq(s):  # 词频统计函数
    s_list = s.split('/')  # 以"/"为分界将字符串变成列表
    #[s_list.remove(item) for item in s_list if item in ',.']  # 将',.'去除
    dic = collections.Counter(s_list)  # 利用Counter函数统计个数
    return dic  # 返回字典


def showInBar(seachname, result):
    '''
    制作柱状图
    :param seachname:
    :param result:
    :return:
    '''
    result = dict(result)
    attr = list(result.keys())[:10]
    v1 = list(result.values())[:10]
    bar = Bar("{}岗位".format(seachname), "需要掌握的语言/工具")
    bar.add(
        "语言/工具",
        attr,
        v1,
        mark_line=["average"],
        mark_point=[
            "max",
            "min"],
        xaxis_rotate=30)
    bar.render("{}.html".format(seachname))


def showInWordCount(seachname, result):
    '''
    制作词云
    :param seachname:
    :param result:
    :return:
    '''
    result = dict(result)
    name = list(result.keys())[:30]
    value = list(result.values())[:30]
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[20, 100])
    wordcloud.render("{}wordcloud.html".format(seachname))


def showInBrowser(seachname):
    '''
    打开浏览器显示
    :param seachname:
    :return:
    '''
    webbrowser.open("{}wordcloud.html".format(seachname))
    webbrowser.open("{}.html".format(seachname))


if __name__ == '__main__':
    pywork.drop()
    seachname = input("请输入需要查询的岗位：")
    print("正在搜索{}...".format(seachname))
    getLink(seachname,20)
    URLList = getDetailUrl()
    pool = Pool()

    demands_text = ""
    pool.map(partial(getInfo, demands_text=demands_text), URLList)
    print(demands_text)
    input = open('demands.txt','rb').read()
    CutWordByJieBa(txt=input, seachname=seachname)
    os.remove('demands.txt')
