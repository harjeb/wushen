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
    s.Click(j['selectserver'])
    s.wait(5)
    try:
        s.wait_element(j['role'], 15)
    except:
        s.wait(1)
    s.Click(j['selectrole'])
    s.wait(2)

def dailyquest():
    s.Click(j['showtool'])
    s.Click(j['quest'])

    #副本
    for i in xrange(11):
        s.Click(j['jh'])
        s.Click(j['fb'])
        fb1()
        print 'finish %s' % str(i+1)
    #师门
    s.Click("//span[text()='江湖']")
    s.Click("//span[@for='0']")
    s.Click("//div[text()='逍遥派']")
    s.Click("//span[@cmd='jh fam 5 start']")
    i=1
    while i<=0:
        s.wait(1)
        s.Click("//span[text()='聪辩老人 苏星河']")
        s.Click("//span[text()='师门任务']")
        s.Click("//span[text()='师门任务']")
        s.wait(3)
        try:
            # give=(By.XPATH,"//span[contains(text(),'上交')]")
            # WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located(give))
            s.Click("//span[contains(text(),'上交')]")
            s.Click("//*[name()='svg']/*[name()='text' and @dir='north']")
            s.wait(1)
            s.Click("//*[name()='svg']/*[name()='text' and @dir='south']")
            i+=1
            print 'finish %s' % str(i + 1)
        except:
            s.Click("//span[text()='放弃']")
            s.Click("//*[name()='svg']/*[name()='text' and @dir='north']")
            s.wait(1)
            s.Click("//*[name()='svg']/*[name()='text' and @dir='south']")



def restore():
    hp = s.Click("//div[@itemid='rbzs267b889']//div[@class='progress hp']/div")
    if not hp.is_displayed():
        s.Click("//span[@command='showcombat']")
        s.wait(1)
        hp = s.Click("//div[@itemid='rbzs267b889']//div[@class='progress hp']/div")
    s.wait(2)
    try:
        chp=hp.get_attribute('style')
        chp=chp.split("width:")[1].split("%;")[0]
        chp.strip()
        print chp
        if float(chp)<=90:
            try:
                s.Click("//span[@cmd='liaoshang']")
            except:
                s.Click("//span[@command='showcombat']")
                s.Click("//span[@cmd='liaoshang']")
        s.wait(1)
        try:
            a=(By.XPATH,"//span[@command='stopstate']")
            WebDriverWait(driver, 15, 0.5).until_not(EC.presence_of_element_located(a))
        except:
            pass
    except:
        pass
    s.Click("//span[@cmd='dazuo']")
    s.wait(8)
    b=(By.XPATH,"//hig[contains(text(),'内力')]")
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(b))
    stop=s.Click("//span[@command='stopstate']")
    if stop.is_displayed():
        stop.click()


def kill():
    s.Click("//span[contains(@cmd,'kill')]").
    bodyE=(By.XPATH,"//span[@class='item-name']/wht[contains(text(),'尸体')]")
    WebDriverWait(driver, 300, 0.5).until(EC.presence_of_element_located(bodyE))
    body = s.Click("//span[@class='item-name']/wht[contains(text(),'尸体')]")
    body.click()
    s.Click("//span[contains(@cmd,'get all from')]")


def fb1():
    s.Click("//div[contains(@class,'fb-item') and @index='1']")
    s.Click("//span[@cmd='jh fb 1 start1']")
    s.wait(2)
    s.Click("//span[@class='dialog-close glyphicon glyphicon-remove-circle']")
    s.Click("//span[@cmd='cr yz/cuifu/caizhu']")
    s.wait(10)
    s.Click("//*[name()='svg']/*[name()='text' and @dir='north']")
    s.Click("//span[text()='管家']")
    kill()
    s.Click("//*[name()='svg']/*[name()='text' and @dir='north']")
    s.Click("//span[text()='财主 崔员外']")
    kill()
    s.Click("//cmd[@cmd='look men']")
    try:
        menE = (By.XPATH, "//span[@cmd='open men']")
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(menE))
        tai = s.Click("//span[@cmd='open men']")
        tai.click()
        s.Click("//*[name()='svg']/*[name()='text' and @dir='east']")
        s.Click("//span[text()='答应她']")
        s.Click("//*[name()='svg']/*[name()='text' and @dir='west']")
        s.Click("//*[name()='svg']/*[name()='text' and @dir='south']")
        s.Click("//*[name()='svg']/*[name()='text' and @dir='south']")
        s.Click("//span[text()='答应她']")
        s.Click("//*[name()='svg']/*[name()='text' and @dir='north']")
        s.Click("//*[name()='svg']/*[name()='text' and @dir='north']")
    except:
        pass
    s.Click("//*[name()='svg']/*[name()='text' and @dir='west']")
    s.Click("//span[text()='财主女儿 崔莺莺']")
    s.Click("//span[text()='询问东厢']")
    kill()
    s.Click("//*[name()='svg']/*[name()='text' and @dir='east']")
    s.Click("//*[name()='svg']/*[name()='text' and @dir='east']")
    try:
        s.Click("//cmd[@cmd='look gui']")
        menE = (By.XPATH, "//span[@cmd='search gui']")
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(menE))
        tai = s.Click("//span[@cmd='search gui']")
        tai.click()
        s.wait(3)
    except:
        pass
    s.Click("//span[@cmd='cr']")
    s.Click("//span[@cmd='cr over']")

def fb3():
    s.Click("//div[contains(@class,'fb-item') and @index='3']")
    s.Click("//span[@cmd='jh fb 3 start1']")
    s.wait(2)
    s.Click("//span[@class='dialog-close glyphicon glyphicon-remove-circle']")
    s.Click("//span[@cmd='cr yz/lcy/dating']")
    restore()
    #fb3
    s.Click("//span[text()='丽春院老板娘 韦春芳']")
    kill()
    s.Click("//*[name()='svg']/*[name()='text' and @dir='up']")
    s.Click("//span[text()='龟公']")
    kill()
    s.Click("//*[name()='svg']/*[name()='text' and @dir='west']")
    s.Click("//span[text()='黑龙鞭 史松']")
    kill()
    restore()
    s.Click("//cmd[@cmd='look tai']")
    taiE=(By.XPATH,"//span[@cmd='tui tai']")
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(taiE))
    tai = s.Click("//span[@cmd='tui tai']")
    tai.click()
    s.Click("//*[name()='svg']/*[name()='text' and @dir='enter']")
    s.Click("//span[text()='朝廷逃犯 茅十八']")
    kill()
    s.wait(3)
    s.Click("//span[@cmd='cr']")
    s.Click("//span[@cmd='cr over']")



login()
dailyquest()

