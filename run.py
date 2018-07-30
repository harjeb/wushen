#coding:utf-8

import re
from sele import webutils
import json

j = json.load(open('config.json'))
s = webutils()
def login():
    s.getUrl('http://game.wsmud.com')
    s.wait(3)
    s.Send_Keys(j['username'],j['usernameT'])
    s.Send_Keys(j['password'],j['passwordT'])
    s.Click(j['login'])
    s.wait(2)
    s.Click(j['region'])
    s.wait(2)
    s.Click(j['selectServer'])
    s.wait(5)
    try:
        s.wait_element(j['role'], 15)
    except:
        s.wait(1)
    s.Click(j['selectrole'])
    s.wait(2)


def buyfood():
    # 买食物
    try:
        s.Click(j['jh'])
    except:
        s.Click(j['showtool'])
        s.Click(j['jh'])

    s.Click(j['jhtab'])
    s.Click(j['yangzhou'])
    s.Click(j['enter0'])
    s.Click(j['north'])
    s.Click(j['north'])
    s.Click(j['east'])
    s.Click(j[u'店小二'])
    s.Click(j['buy'])
    buylist = [j[u'米饭'], j[u'米酒'], j[u'包子'], j[u'扬州炒饭'], j[u'鸡腿'],j[u'面条'],j[u'花雕酒']]
    for i in buylist:
        s.Click(i)
        s.Click(j['confirmbuy'])
        s.Send_Keys(j['buy5'], '5')
        s.Click(j['ok'])
    # 买养精丹
    s.Click(j['close'])
    s.Click(j['west'])
    s.Click(j['south'])
    s.Click(j['south'])
    s.Click(j['east'])
    s.Click(j['east'])
    s.Click(j['north'])
    s.Click(j[u'平一指'])
    s.Click(j['buy'])
    s.Click(j[u'养精丹'])
    s.Click(j['confirmbuy'])
    s.Send_Keys(j['buy5'], '10')
    s.Click(j['ok'])
    s.Click(j['close'])
    s.Click(j['bag'])
    for i in xrange(10):
        s.Click(j[u'养精丹bag'])
        s.Click(j['use'])






def shimen():
    # 师门
    s.Click(j['jh'])
    s.Click(j['jhtab'])
    s.Click(j['xiaoyao'])
    s.Click(j['enter5'])
    i = 1
    while i <= 20:
        s.wait(1)
        s.Click(j[u'苏星河'])
        s.Click(j[u'师门任务'])
        s.Click(j[u'师门任务'])
        s.wait(3)
        try:
            # give=(By.XPATH,"//span[contains(text(),'上交')]")
            # WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located(give))
            s.Click(j[u'上交'])
            s.Click(j['north'])
            s.wait(1)
            s.Click(j['south'])
            i += 1
            print '师门任务完成 %s 次' % str(i - 1)
        except:
            s.Click(j['giveup'])
            s.Click(j['north'])
            s.wait(0.5)
            s.Click(j['south'])

def fb():
    #副本
    if not s.get_display(j['jh']):
        s.Click(j['showtool'])
    for i in xrange(20):
        s.Click(j['jh'])
        s.Click(j['fb'])
        fb1()
        print '副本完成 %s 次' % str(i+1)
        if (i+1)%3==0:
            cleanbag()

def dailyquest():
    #stop state
    stop=s.find_element(j['stop'])
    if stop.is_displayed():
        stop.click()
    # buyfood()
    shimen()
    fb()

def restore():
    if not s.get_display(j['hp']):
        s.Click(j['showcombat'])
        s.wait(1)
    s.wait(2)
    try:
        chp=s.get_attribute(j['hp'],'style')
        chp=chp.split("width:")[1].split("%;")[0]
        chp.strip()
        if float(chp)<=90:
            try:
                print '当前血量 %s, 开始疗伤回血' % str(chp)
                s.Click(j['liaoshang'])
            except:
                s.Click(j['showcombat'])
                s.Click(j['liaoshang'])
        s.wait(1)
        try:
            s.untilnot(j['stop'])
        except:
            pass
    except:
        pass
    cmp=s.get_attribute(j['mp'],'style')
    cmp=cmp.split("width:")[1].split("%;")[0]
    cmp.strip()
    if float(cmp)<=70:
        try:
            s.Click(j['dazuo'])
            s.wait(12)
            s.wait_element(j[u'内力'])
            stop=s.find_element(j['stop'])
            if stop.is_displayed():
                stop.click()
        except:
            print 'dazuo error...'


def kill():
    s.Click(j['kill'])
    # s.wait_element(j['body'],seconds=300)
    # s.Click(j['body'])
    # s.Click(j['loot'])


def cleanbag():
    try:
        s.Click(j['jh'])
    except:
        s.Click(j['showtool'])
        s.Click(j['jh'])
    s.Click(j['jhtab'])
    s.Click(j['yangzhou'])
    s.Click(j['enter0'])
    s.Click(j['east'])
    s.Click(j['south'])
    s.Click(j[u'杨永福'])
    s.Click(j['buy'])
    s.Click(j['sellall'])

def fb1():
    s.Click(j['fb1'])
    s.Click(j['fb1s'])
    s.wait(2)
    s.Click(j['close'])
    s.Click(j['fb1g'])
    s.wait(10)
    s.Click(j['north'])
    s.Click(j[u'管家'])
    kill()
    s.Click(j['north'])
    s.Click(j[u'崔员外'])
    kill()
    s.Click(j['lookmen'])
    try:
        s.wait_element(j['openmen'], seconds=20)
        s.Click(j['openmen'])
        s.Click(j['east'])
        s.Click(j[u'答应她'])
        s.Click(j['west'])
        s.Click(j['south'])
        s.Click(j['south'])
        s.Click(j[u'答应她'])
        s.Click(j['north'])
        s.Click(j['north'])
    except:
        pass
    s.Click(j['west'])
    s.Click(j[u'崔莺莺'])
    s.Click(j['askeast'])
    kill()
    s.Click(j['east'])
    try:
        s.Click(j['east'])
        s.Click(j['lookgui'])
        s.wait_element(j['searchgui'], seconds=20)
        s.Click(j['searchgui'])
        s.wait(3)
    except:
        pass
    s.Click(j['cr'])
    s.Click(j['crover'])

def fb3():
    s.Click(j['fb3'])
    s.Click(j['fb3s'])
    s.wait(2)
    s.Click(j['close'])
    s.Click(j['fb3g'])
    restore()
    #fb3
    s.Click(j[u'韦春芳'])
    kill()
    s.Click(j['up'])
    s.Click(j[u'龟公'])
    kill()
    s.Click(j['west'])
    s.Click(j[u'史松'])
    kill()
    restore()
    s.Click(j['looktai'])
    s.wait_element(j['tuitai'], seconds=20)
    s.Click(j['tuitai'])
    s.Click(j['enter'])
    s.Click(j[u'茅十八'])
    kill()
    s.wait(3)
    s.Click(j['cr'])
    s.Click(j['crover'])

if __name__ == "__main__":
    login()
    dailyquest()


