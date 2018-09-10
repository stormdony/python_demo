from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('localhost', 27017)
zhipin = client['zhipin']
zhipin_java = zhipin['zhipin_java']
zhipin_python = zhipin['zhipin_python']


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

total_page = 11


def get_info(param, data_table):
    '''
    根据招聘方向(java或python..)爬取信息存进数据库
    :param param: 招聘方向
    :param data_table: 数据库表明
    :return:
    '''
    for i in range(1, total_page):
        url = 'https://www.zhipin.com/c101280100/d_203-h_101280100/?query={0}&page={1}'.format(
            param, i)
        web_data = requests.get(url, headers=headers)
        soup = BeautifulSoup(web_data.content, 'lxml')
        for item in soup.select('#main > div > div.job-list > ul > li'):
            # 招聘要求
            job_title = item.select('.job-title')[0].text  # 岗位
            salary = item.select('.red')[0].text  # 薪资
            person_info = item.select('.info-primary p')[0].text  # 应聘要求
            # 获取公司信息
            company = item.select('.info-company h3 a')[0].text  # 公司
            company_info = item.select('.info-company p')[0].text  # 公司信息

            data = {
                'job_title': job_title,
                'salary': salary,
                'person_info': person_info,
                'company': company,
                'company_info': company_info,
            }
            # 插入数据库
            data_table.insert(data)
            print(data)
        print('*' * 100)
    print('\n' * 5)


if __name__ == '__main__':
    param_list = ['java', 'python']
    table_list = [zhipin_java, zhipin_python]
    for param, table in zip(param_list, table_list):
        get_info(param, table)

