'''
Author: Don Lex
微信公众号：Python绿洲

本程序不是所有的账号都适用，请根据实际情况修改相应的代码

'''


from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

URL = 'http://ui.ptlogin2.qq.com/cgi-bin/login?appid=614038002&style=9&s_url=http%3A%2F%2Fdld.qzapp.z.qq.com%2Fqpet%2Fcgi-bin%2Fphonepk%3Fcmd%3Dindex%26channel%3D0'
username = '账号'
pwd = '密码'

driver = webdriver.Chrome()
driver.implicitly_wait(5)


def login(url, username, pwd):
    driver.get(url)
    driver.find_element_by_id('u').clear()
    driver.find_element_by_id('u').send_keys(username)
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys(pwd)
    driver.find_element_by_id('go').click()
    sleep(2)

# 领取徒弟经验
def ling_qu_tu_di():
    try:
        driver.find_element_by_link_text('领取徒弟经验').click()
        sleep(1)
    except NoSuchElementException:
        print("meiyou_tu_di")


# 每日奖励
def mei_ri_jing_yan():
    try:
        driver.find_element_by_link_text('每日奖励').click()
    except NoSuchElementException:
        print('没有找到每日奖励')
    sleep(1)
    try:
        for i in range(0, 2):
            driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[2]').click()
            sleep(1)
    except NoSuchElementException:
        print('没有找到每日奖励领取按钮')
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 乐斗好友
def flight():
    for i in range(6, 16):
        myfriend = driver.find_element_by_link_text('好友')
        myfriend.click()
        driver.find_element_by_link_text("下页").click()
        sleep(1)
        driver.find_element_by_xpath(
            ' // *[ @ id = "id"] / a[{}]'.format(i)).click()
        sleep(1)
        driver.find_element_by_link_text('返回大乐斗首页').click()


#     历练
def lilian():
    driver.find_element_by_link_text('历练').click()
    sleep(1)
    driver.find_element_by_link_text('鹅王的试炼').click()
    sleep(1)
    driver.find_element_by_link_text('下一页').click()
    sleep(1)
    for i in range(0, 5):
        driver.find_element_by_xpath('//*[@id="id"]/a[10]').click()
        sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 重出江湖
def call_back():
    driver.find_element_by_link_text('重出江湖').click()
    sleep(1)
    for i in range(0, 3):
        driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[5]').click()
        sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 抢地盘
def dipan():
    driver.find_element_by_link_text('抢地盘').click()
    driver.find_element_by_xpath('//*[@id="id"]/a[17]').click()
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 许愿
def xuyuan():
    driver.find_element_by_link_text('许愿').click()
    sleep(1)
    driver.find_element_by_link_text('领取许愿奖励').click()
    sleep(1)
    driver.find_element_by_link_text('许愿').click()
    sleep(1)
    driver.find_element_by_link_text('向月敏上香许愿').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/a[1]').click()  # 领取
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


#     斗神塔
def flight_ta():
    driver.find_element_by_link_text('斗神塔').click()
    sleep(1)
    driver.find_element_by_link_text('结束挑战').click()
    sleep(1)
    driver.find_element_by_link_text('取消').click()
    sleep(1)
    driver.find_element_by_link_text('自动挑战').click()
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 十二宫
def gong():
    driver.find_element_by_link_text('十二宫').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[25]').click()
    sleep(1)
    driver.find_element_by_link_text('请猴王扫荡').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/p[1]/a').click()  # 复活
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[3]').click()  # 选择剑君复活
    sleep(1)
    driver.find_element_by_link_text('确认复活').click()  # 确认复活
    sleep(1)
    driver.find_element_by_link_text('返回十二宫').click()  # 返回十二宫
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[25]').click()
    sleep(1)
    driver.find_element_by_link_text('请猴王扫荡').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/p[1]/a').click()
    sleep(1)
    driver.find_element_by_link_text('直接结束')
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


#     问鼎天下
def tian_xia():
    driver.find_element_by_link_text('问鼎天下').click()
    sleep(1)
    for i in range(0, 5):
        driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[18]').click()  # 攻占
        sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()

# 竞技场
def jin_ji_chang():
    driver.find_element_by_link_text('竞技场').click()
    sleep(1)
    for i in range(0, 5):
        driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[3]').click()  # 免费挑战
        sleep(1)
    driver.find_element_by_link_text('领取奖励').click()
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 镖行天下
def biao_xing_tian_xia():
    driver.find_element_by_link_text('镖行天下').click()
    sleep(1)
    driver.find_element_by_link_text('护送完成').click()
    sleep(1)
    driver.find_element_by_link_text('领取奖励').click()
    sleep(1)
    driver.find_element_by_link_text('护送押镖').click()
    sleep(1)
    driver.find_element_by_link_text('刷新押镖').click()
    sleep(1)
    driver.find_element_by_link_text('启程护送').click()
    sleep(1)
    driver.find_element_by_link_text('刷新').click()
    sleep(1)
    for i in range(6, 12, 2):
        driver.find_element_by_xpath(
            '//*[@id="id"]/p/a[{}]'.format(i)).click()  # 拦截
        sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 幻境
def huan_jing():
    driver.find_element_by_link_text('幻境').click()
    sleep(1)
    driver.find_element_by_link_text('乐斗村').click()
    sleep(1)
    for i in range(0, 5):
        driver.find_element_by_xpath('//*[@id="id"]/p/a[4]').click()  # 拦截
        sleep(1)
    driver.find_element_by_link_text('返回飘渺幻境').click()
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 画卷迷踪
def hua_juan_mi_zong():
    driver.find_element_by_link_text('画卷迷踪').click()
    sleep(1)
    for i in range(0, 5):
        driver.find_element_by_link_text('准备完成进入战斗').click()
        sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 门派邀请赛
def men_pai_yao_qing_sai():
    driver.find_element_by_link_text('门派邀请赛').click()
    sleep(1)
    for i in range(0, 5):
        driver.find_element_by_link_text('开始挑战').click()
        sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 门派
def men_pai():
    driver.find_element_by_link_text("门派").click()
    sleep(1)
    driver.find_element_by_link_text('龙头香').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[1]').click()  # 点燃
    sleep(1)
    driver.find_element_by_link_text('返回门派首页').click()
    sleep(1)
    driver.find_element_by_link_text('琼台观').click()
    sleep(1)
    driver.find_element_by_link_text('进入木桩训练').click()
    sleep(1)
    driver.find_element_by_link_text('进入同门切磋').click()
    sleep(1)
    driver.find_element_by_link_text('返回门派首页').click()
    sleep(1)
    driver.find_element_by_link_text('金殿').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[1]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[2]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[4]').click()
    sleep(1)
    driver.find_element_by_link_text('返回门派首页').click()
    sleep(1)
    driver.find_element_by_link_text('玉虚宫').click()
    sleep(1)
    try:
        driver.find_element_by_link_text('完成').click()
    except BaseException:
        pass
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 梦想之旅
def meng_xiang_zhi_lv():
    driver.find_element_by_link_text('梦想之旅').click()
    sleep(1)
    driver.find_element_by_link_text('普通旅行').click()
    sleep(1)
    driver.find_element_by_link_text('梦幻旅行').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[5]').click()
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 任务
def ren_wu():
    driver.find_element_by_link_text('任务').click()
    sleep(1)
    driver.find_element_by_link_text('一键完成任务').click()
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 武林大会
def wu_lin_da_hui():
    driver.find_element(
        By.XPATH,
        "//a[contains(@href,'fastSignWulin')]").click()
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 分享
def share():
    driver.find_element_by_link_text('分享').click()
    sleep(1)
    driver.find_element_by_link_text('一键分享').click()
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 领奖
def ling_jiang():
    driver.find_element_by_link_text('领奖').click()
    sleep(1)
    for i in range(0, 2):
        driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[1]').click()
        sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 群雄逐鹿
def qun_xiong_zhu_lu():
    driver.find_element_by_link_text('群雄逐鹿').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[1]').click()  # 报名
    sleep(1)
    driver.find_element_by_link_text('领奖').click()
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# # 会武
def hui_wu():
    driver.find_element_by_link_text('会武').click()
    sleep(1)
    driver.find_element_by_link_text('初级试炼场').click()
    sleep(1)
    for i in range(0, 6):
        driver.find_element_by_link_text('挑战').click()
        sleep(1)
    driver.find_element_by_link_text('冠军助威').click()
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 挑战陌生人
def mo_sheng_ren():
    driver.find_element_by_link_text('斗友').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="id"]/a[7]').click()
    sleep(1)
    driver.find_element_by_xpath(' //*[@id="id"]/a[13]').click()
    sleep(1)
    driver.find_element_by_xpath(' //*[@id="id"]/a[14]').click()
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 找菜菜做菜
def zhao_cai_cai_zuo_cai():
    driver.find_element_by_link_text('我的帮派').click()
    sleep(1)
    driver.find_element_by_link_text('帮派守护神').click()
    sleep(1)
    driver.find_element_by_link_text('享受菜菜大餐').click()
    sleep(1)
    driver.find_element_by_link_text('帮派守护神').click()
    sleep(1)
    driver.find_element_by_link_text('找菜菜做菜').click()
    sleep(1)
    driver.find_element_by_link_text('返回大乐斗首页').click()


# 乐斗帮友
def flightBangYou():
    driver.find_element_by_link_text('帮友').click()
    for i in range(6, 11):
        driver.find_element_by_xpath('//*[@id="id"]/a[{}]'.format(i)).click()
        sleep(1)


# 所有任务
def All_Task():
    login(URL, username, pwd)  # 登录
    sleep(1)
    ling_qu_tu_di()  # 领取徒弟经验
    mei_ri_jing_yan()  # 领取经验
    wu_lin_da_hui()  # 武林大会
    men_pai()  # 门派   完成任务
    flight()  # 乐斗好友
    flightBangYou()  # 乐斗帮友
    call_back()  # 重回乐斗
    dipan()  # 抢地盘
    xuyuan()  # 许愿
    qun_xiong_zhu_lu()  # 群雄逐鹿
    lilian()  # 历练
    gong()  # 十二宫  结束
    flight_ta()  # 斗神塔
    tian_xia()  # 问鼎天下
    jin_ji_chang()  # 竞技场   #TODO 待调试
    biao_xing_tian_xia()  # 镖行天下
    zhao_cai_cai_zuo_cai()  # 找菜菜做菜
    mo_sheng_ren()  # 挑战陌生人
    meng_xiang_zhi_lv()  # 梦想之旅
    hua_juan_mi_zong()  # 画卷迷踪
    huan_jing()  # 幻境
    share()  # 分享
    ren_wu()  # 任务
    ling_jiang()  # 活跃度领奖


if __name__ == "__main__":
    All_Task()
