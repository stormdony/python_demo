'''
@ Auther : Don Lex
site: https://donlex.cn
根据网易云歌曲链接，获取歌词lyric
'''
import re
import requests
import json

class neteasse:
    def __init__(self, url):
        self.url = url
        self.link = 'http://music.163.com/api/song/media?id='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}

    def get_song_id(self):
        '''
        根据传入的链接，截取出歌曲的id
        :param url: str
        :return: str
        '''
        # 'https://music.163.com/#/song?id=863046037'
        if self.url != "":
            id = re.split('id=', self.url)[1]
            return id
        else:
            return ""

    def get_lyrics(self):
        '''
        根据歌曲id，请求获取歌词
        :param id: str
        :return: str
        '''
        id = self.get_song_id()
        if id != "":
            self.link += id
            web_data = requests.get(url=self.link, headers=self.headers).text
            json_data = json.loads(web_data)
            try:
                return json_data['lyric']
            except BaseException:
                return "歌曲id错误,请检查后重试！！！"
        else:
            return "链接错误,请检查后重试！！！"


if __name__ == '__main__':
    url = 'https://music.163.com/#/song?id=863046037'
    net = neteasse(url)
    lyric = net.get_lyrics()
    print(lyric)
