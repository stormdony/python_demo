import json
import time
import requests
from bs4 import BeautifulSoup as BS
from urllib import parse


def get_appinf(filename):
    f = open(filename, 'r', encoding='utf-8')
    try:
        j = json.loads(f.read())
        #判断数据文件是否有题目和选项
        if 'quiz' in j['data'] and 'options' in j['data']:
            num = j['data']['num']
            quiz = j['data']['quiz']
            print(('第'+str(num)+'题：'+quiz).center(50,'*')+'\n')
            cho = j['data']['options']
        else:
            pass
        return quiz,cho
    except:
        pass
        print('还没开始呢**********')
    f.close()




def begin(filename):
    f = open(filename, 'r', encoding='utf-8')
    try:
        j = json.loads(f.read())
        # 判断数据文件是否有题目和选项
        if 'quiz' in j['data'] and 'options' in j['data']:
            num = j['data']['num']
            quiz = j['data']['quiz']
            print(('第' + str(num) + '题：' + quiz).center(50, '*') + '\n')
            cho = j['data']['options']
            pagenum = [0, 10, 20]
            ans = []
            A = 0
            B = 0
            C = 0
            D = 0
            for i in pagenum:
                url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=' + quiz[:-1] + '&pn={}'.format(i)
                wb_data = requests.get(url)
                wb_data.encoding = 'utf-8'
                content = wb_data.text
                for index,choice in enumerate(cho):
                    strnum = content.count(choice)
                    # print(choice + " : {}".format(strnum))
                    ans.append(strnum)
            for index,selection in enumerate(ans):
                index = (index % 4)
                if index == 0:
                    D += selection
                elif index == 1:
                    C += selection
                elif index == 2:
                    B += selection
                elif index == 3:
                    A += selection
            number = [D, C, B, A]
            for name, count in zip(cho, number):
                print(name, count)
            index = number.index(max(number))
            print('\033[32;0m')
            print(("    应该选第    " + str((index + 1)) + "  个     " + str(cho[index])).center(50, '*'))
            print('\033[0m ')
        else:
            pass
            print('  -  '*15)
    except:
        pass
    f.close()

if __name__ == '__main__':
    while True:
        begin('D:/quiz/body.txt')
        time.sleep(1)