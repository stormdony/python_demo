import requests
from bs4 import BeautifulSoup
import codecs
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Connection': 'close'}

def get_link(url):
    '''获取全部章节的链接'''
    html = s.get(url)
    soup = BeautifulSoup(html.content, 'lxml')  # content如果换成text会有乱码
    url_list = []
    list = soup.select("#list > dl > dd > a")
    for i in list:
        i = i.get("href")
        i = 'http://www.biqugecom.com' + i
        url_list.append(i)
    url_list = url_list[9:-1]
    return url_list

def get_data(url):
    '''获取详细文本'''
    html = s.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    f = codecs.open('output.txt', 'a+', 'utf-8')
    # 以二进制写入章节题目 需要转换为utf-8编码，否则会出现乱码
    section_name = soup.select("#wrapper > div.content_read > div > div.bookname > h1")[0].text
    print(section_name)
    f.write(('\r\n' + section_name + '\r\n'))
    section_text = soup.select("#content")
    for x in section_text:
        a = x.text.replace('readx();', '').replace('www.biqugecom.com/27/27204/', '')
        # 以二进制写入章节内容
        f.write((a)+ '\r\n')
    f.close()  # 关闭小说文件

if __name__ == '__main__':
    url = 'http://www.biqugecom.com/27/27204/'
    url_list = get_link(url)
    for i in url_list:
        get_data(i)