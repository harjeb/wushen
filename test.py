#coding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
def login():
    driver.get('http://game.wsmud.com')
    time.sleep(5)
    driver.find_element_by_xpath("//input[@id='login_name']").send_keys('harjeb')
    driver.find_element_by_xpath("//input[@id='login_pwd']").send_keys('6504970')
    driver.find_element_by_xpath("//span[text()='登陆']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//li[contains(text(),'二区')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//li[@command='SelectServer']").click()
    time.sleep(5)
    try:
        driver.implicitly_wait(15)
        driver.find_element_by_xpath("//li[contains(text(),'中央书记')]")
    except:
        time.sleep(1)
    driver.find_element_by_xpath("//li[@command='SelectRole']").click()
    time.sleep(2)
    driver.save_screenshot('login.png')

def dailyquest():
    driver.find_element_by_xpath("//span[@command='showtool']").click()
    driver.find_element_by_xpath("//span[text()='任务']").click()
    driver.save_screenshot('quest.png')

    #副本
    for i in xrange(11):
        driver.find_element_by_xpath("//span[text()='江湖']").click()
        driver.find_element_by_xpath("//span[text()='副本']").click()
        fb1()
        print 'finish %s' % str(i+1)
    #师门
    driver.find_element_by_xpath("//span[text()='江湖']").click()
    driver.find_element_by_xpath("//span[@for='0']").click()
    driver.find_element_by_xpath("//div[text()='逍遥派']").click()
    driver.find_element_by_xpath("//span[@cmd='jh fam 5 start']").click()
    i=1
    while i<=0:
        time.sleep(1)
        driver.find_element_by_xpath("//span[text()='聪辩老人 苏星河']").click()
        driver.find_element_by_xpath("//span[text()='师门任务']").click()
        driver.find_element_by_xpath("//span[text()='师门任务']").click()
        driver.implicitly_wait(3)
        try:
            # give=(By.XPATH,"//span[contains(text(),'上交')]")
            # WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located(give))
            driver.find_element_by_xpath("//span[contains(text(),'上交')]").click()
            driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='north']").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='south']").click()
            i+=1
            print 'finish %s' % str(i + 1)
        except:
            driver.find_element_by_xpath("//span[text()='放弃']").click()
            driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='north']").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='south']").click()



def restore():
    hp = driver.find_element_by_xpath("//div[@itemid='rbzs267b889']//div[@class='progress hp']/div")
    if not hp.is_displayed():
        driver.find_element_by_xpath("//span[@command='showcombat']").click()
        time.sleep(1)
        hp = driver.find_element_by_xpath("//div[@itemid='rbzs267b889']//div[@class='progress hp']/div")
    time.sleep(2)
    try:
        chp=hp.get_attribute('style')
        chp=chp.split("width:")[1].split("%;")[0]
        chp.strip()
        print chp
        if float(chp)<=90:
            try:
                driver.find_element_by_xpath("//span[@cmd='liaoshang']").click()
            except:
                driver.find_element_by_xpath("//span[@command='showcombat']").click()
                driver.find_element_by_xpath("//span[@cmd='liaoshang']").click()
        time.sleep(1)
        try:
            a=(By.XPATH,"//span[@command='stopstate']")
            WebDriverWait(driver, 15, 0.5).until_not(EC.presence_of_element_located(a))
        except:
            pass
    except:
        pass
    driver.find_element_by_xpath("//span[@cmd='dazuo']").click()
    time.sleep(8)
    b=(By.XPATH,"//hig[contains(text(),'内力')]")
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(b))
    stop=driver.find_element_by_xpath("//span[@command='stopstate']")
    if stop.is_displayed():
        stop.click()


def kill():
    driver.find_element_by_xpath("//span[contains(@cmd,'kill')]").click()
    bodyE=(By.XPATH,"//span[@class='item-name']/wht[contains(text(),'尸体')]")
    WebDriverWait(driver, 300, 0.5).until(EC.presence_of_element_located(bodyE))
    body = driver.find_element_by_xpath("//span[@class='item-name']/wht[contains(text(),'尸体')]")
    body.click()
    driver.find_element_by_xpath("//span[contains(@cmd,'get all from')]").click()


def fb1():
    driver.find_element_by_xpath("//div[contains(@class,'fb-item') and @index='1']").click()
    driver.find_element_by_xpath("//span[@cmd='jh fb 1 start1']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[@class='dialog-close glyphicon glyphicon-remove-circle']").click()
    driver.find_element_by_xpath("//span[@cmd='cr yz/cuifu/caizhu']").click()
    time.sleep(10)
    driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='north']").click()
    driver.find_element_by_xpath("//span[text()='管家']").click()
    kill()
    driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='north']").click()
    driver.find_element_by_xpath("//span[text()='财主 崔员外']").click()
    kill()
    driver.find_element_by_xpath("//cmd[@cmd='look men']").click()
    try:
        menE = (By.XPATH, "//span[@cmd='open men']")
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(menE))
        tai = driver.find_element_by_xpath("//span[@cmd='open men']")
        tai.click()
        driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='east']").click()
        driver.find_element_by_xpath("//span[text()='答应她']").click()
        driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='west']").click()
        driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='south']").click()
        driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='south']").click()
        driver.find_element_by_xpath("//span[text()='答应她']").click()
        driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='north']").click()
        driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='north']").click()
    except:
        pass
    driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='west']").click()
    driver.find_element_by_xpath("//span[text()='财主女儿 崔莺莺']").click()
    driver.find_element_by_xpath("//span[text()='询问东厢']").click()
    kill()
    driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='east']").click()
    driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='east']").click()
    try:
        driver.find_element_by_xpath("//cmd[@cmd='look gui']").click()
        menE = (By.XPATH, "//span[@cmd='search gui']")
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(menE))
        tai = driver.find_element_by_xpath("//span[@cmd='search gui']")
        tai.click()
        time.sleep(3)
    except:
        pass
    driver.find_element_by_xpath("//span[@cmd='cr']").click()
    driver.find_element_by_xpath("//span[@cmd='cr over']").click()

def fb3():
    driver.find_element_by_xpath("//div[contains(@class,'fb-item') and @index='3']").click()
    driver.find_element_by_xpath("//span[@cmd='jh fb 3 start1']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[@class='dialog-close glyphicon glyphicon-remove-circle']").click()
    driver.find_element_by_xpath("//span[@cmd='cr yz/lcy/dating']").click()
    restore()
    #fb3
    driver.find_element_by_xpath("//span[text()='丽春院老板娘 韦春芳']").click()
    kill()
    driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='up']").click()
    driver.find_element_by_xpath("//span[text()='龟公']").click()
    kill()
    driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='west']").click()
    driver.find_element_by_xpath("//span[text()='黑龙鞭 史松']").click()
    kill()
    restore()
    driver.find_element_by_xpath("//cmd[@cmd='look tai']").click()
    taiE=(By.XPATH,"//span[@cmd='tui tai']")
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(taiE))
    tai = driver.find_element_by_xpath("//span[@cmd='tui tai']")
    tai.click()
    driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @dir='enter']").click()
    driver.find_element_by_xpath("//span[text()='朝廷逃犯 茅十八']").click()
    kill()
    time.sleep(3)
    driver.find_element_by_xpath("//span[@cmd='cr']").click()
    driver.find_element_by_xpath("//span[@cmd='cr over']").click()



login()
dailyquest()

