
from multiprocessing.pool import Pool

from pyquery import PyQuery as pq
import pymongo
import logging
client = pymongo.MongoClient('localhost', 27017)
jihaoba = client['pyquery_jihaoba']
detail = jihaoba['detail']


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Connection': 'close'}

# 获取数据，参数为页数
def get_phone(page):
    url = 'http://www.jihaoba.com/escrow/?&page={}'.format(page)
    try:
        web_data = pq(url=url, headers=header)
        phone_lis = web_data('.numbershow')
        for item in phone_lis.items():
            phone = item.find('.number').text()
            price = item.find('.price span').text()
            brand = item.find('.brand').text()
            law = item.find('.law').text()
            data = {
                'phone': phone,#手机号
                'price': price[1:],#价格
                'band': brand,#运营商
                'law': law,#简介
            }
            print(data)
            detail.insert(data)
    except:
        logging.warning('连接的主机没有反应')
        pass


if __name__ == '__main__':
    pool = Pool()
    pool.map(get_phone, [i for i in range(1, 1001)])
