#coding:utf-8
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
   

class webutils():

    def __init__(self, browser='chrome'):
        '''
        :param browser:   浏览器对象
        :return:
        '''
        if browser == "firefox" :
            driver = webdriver.Firefox()
        elif browser == "chrome":
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(r'chromedriver.exe', chrome_options=chrome_options)
        elif browser == "ie" :
            DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
            driver = webdriver.Ie("../resources/drivers/IEDriverServer.exe")
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS(r'phantomjs.exe')
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found this browser,You can enter 'firefox', 'chrome', 'ie' or 'phantomjs'.")

    def getElement(self,value):
        '''

        :param by:     查找元素的方式
        :param value:  文本值
        :return:       查找到的元素
        '''
        by='xpath'

        if by=="id":
            return self.driver.find_element_by_id(value)
        elif by=="class":
            return self.driver.find_element_by_class_name(value)
        elif by=="name":
            return self.driver.find_element_by_name(value)
        elif by=="css":
            return self.driver.find_element_by_css_selector(value)
        elif by=="linktext":
            return self.driver.find_element_by_link_text(value)
        elif by=="partcialtext":
            return self.driver.find_element_by_partial_link_text(value)
        elif by=="tag":
            return self.driver.find_element_by_tag_name(value)
        elif by=='xpath':
            return self.driver.find_element_by_xpath(value)
        elif by=='js'or by=="jquery":
            return self.ExcuteJs(value)
        else:
            print "请输入适合的查找元素方式。。。"

    def ExcuteJs(self,js):
        '''

        :param js:  js查找元素方式，或jQuery
        :return:    找到元素
        '''
        self.driver.execute_script(js)

    def SetTextBox(self,text,value):
        '''
        :param text:     设置文本框的值
        :param by:       查找元素的方式
        :param value:    文本值
        :return:
        '''
        elemet=self.getElement(value)
        self.driver.execute_script("arguments[0].innerHTML = \"" + text + "\"",elemet)

    def getTextBox(self,by,value):
        '''
        :param by:       查找元素的方式
        :param value:    文本值
        :return:         返回富文本框的值
        '''
        elment=self.getElement(value)
        return self.driver.execute_script("arguments[0].innerHTML()",elment)

    def InputByJs(self,value):
        '''
        :param by:     查找元素的方式
        :param value:  文本值
        :return:
        '''
        elment=self.getElement(value)
        self.driver.execute_script("arguments[0].value=\""+value+"\"",elment)

    def scrollToElement(self,value):
        '''
        :param by:     查找元素的方式
        :param value:  文本值
        :return:
        '''
        elment=self.getElement(value)
        self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);",elment)

    def SwitchWindow_Two(self):
        '''
        适用于两个窗口的切换
        :return:
        '''
        CurrentHandle=self.driver.current_window_handle
        handles=self.driver.window_handles
        for handle in  handles:
            if handle==CurrentHandle:
                continue
            else:
                self.driver._switch_to.window(handle)

    def SwitchWindow_By_Tltle(self,Title):
        '''
        :param Title: 浏览器窗口标题
        :return:
        '''
        flag=False
        CurrentHandle=self.driver.current_window_handle
        handles=self.driver.window_handles
        for handle in  handles:
            if handle==CurrentHandle:
                continue
            else:
                self.driver.switch_to_window(handle)
                if Title in self.driver.title:
                    flag=True
                    return flag
        return flag

    def SwitchWindow_By_Url(self,url):
        '''
        :param url:   需要切换窗口的url
        :return:
        '''
        flag=False
        CurrentHandle=self.driver.current_window_handle
        handles=self.driver.window_handles
        for handle in  handles:
            self.driver.switch_to_window(handle)
            if url in self.driver.current_url:
                flag=True
                return  flag
        return  flag

    def max_window(self):
        '''
        :return: 最大化窗口
        '''
        self.driver.maximize_window()

    def getUrl(self,url):
        '''
        :param url: 转向地址
        :return:
        '''
        self.driver.get(url)

    def wait(self,seconds):
        '''
        :param seconds:    等待时间
        :return:
        '''
        time.sleep(seconds)
        #self.driver.implicitly_wait(seconds)

    def Close(self):
        '''
        :return:  关闭窗口
        '''
        self.driver.close()

    def Quit(self):
        '''
        :return:  退出浏览器
        '''
        self.driver.quit()
       
    def exists(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def find_elements(self,element):
        return self.driver.find_elements_by_xpath(element)


    def find_element(self,element):
        """
        Judge element positioning way, and returns the element.

        Usage:
        driver.find_element  此为元组(id,kw)，此方法为PageObject模式准备方法
        """
        #by = element[0]
        #value = element[1]
        by = 'xpath'
        value = element

        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "text":
            return self.driver.find_element_by_link_text(value)
        elif by == "text_part":
            return self.driver.find_element_by_partial_link_text(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")

    def wait_element(self, element, seconds=5):
        """
        等待元素在指定的时间类出现
        :param element:      元素的定位表达式
        :param seconds:      等待的时间
        :return:
        """
        # by = element[0]
        # value = element[1]
        by = 'xpath'
        value = element

        if by == "id":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "text":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

    def untilnot(self, element, seconds=15):
        """
        等待元素在指定的时间类消失
        :param element:      元素的定位表达式
        :param seconds:      等待的时间
        :return:
        """
        WebDriverWait(self.driver, seconds, 0.5).until_not(EC.presence_of_element_located((By.XPATH, element)))



    def Send_Keys(self,element,value):
        '''
        :param element:     元素的定位表达式
        :param value:       输入值
        :return:
        '''
        self.wait_element(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(value)

    def Click(self,element):
        '''
        功能：点击
        :param element: 元素的定位表达式
        :return:
        '''
        self.wait_element(element)
        self.wait(0.5)
        self.find_element(element).click()


    def Right_Click(self,element):
        '''
        功能：右击
        :param element: 元素的定位表达式
        :return:
        '''
        self.wait_element(element)
        ActionChains.context_click(self.find_element(element)).perform()

    def MoveToElement(self,element):
        '''
        功能：移动到元素
        :param element: 元素的定位表达式
        :return:
        '''
        self.wait_element(element)
        ActionChains.move_to_element(self.find_element(element)).perform()

    def double_click(self,element):
        '''
        功能：双击元素
        :param element: 元素的定位表达式
        :return:
        '''
        self.wait_element(element)
        ActionChains.double_click(self.find_element(element)).perform()

    def drag_and_drop(self,element):
        '''
        功能：拖拽元素
        :param element: 元素的表达式
        :return:
        '''
        self.wait_element(element)
        ActionChains.drag_and_drop(self.find_element(element)).perform()

    def back(self):
        '''
        功能：返回
        :return:
        '''
        self.driver.back()

    def forward(self,element):
        '''

        :param element:  元素的表达式
        :return:
        '''

        self.driver.forward()

    def get_attribute(self, element, attribute):
        """
        功能：得到元素的属性值
        :param element:    元素表达式
        :param attribute:  属性名称
        :return:
        """
        self.wait_element(element)
        return self.find_element(element).get_attribute(attribute)

    def get_text(self, element):
        """

        :param element:  元素表达式
        :return:         返回的是元素的文本值
        """

        self.wait_element(element)
        return self.find_element(element).text

    def get_display(self, element):
        """
        功能：判断元素是否显示
        :param element: 元素表达式
        :return:
        """

        self.wait_element(element)
        return self.find_element(element).is_displayed()

    def get_title(self):
        """
        功能:得到浏览器的标题
        :return:
        """
        return self.driver.title

    def get_url(self):
        """
        功能:得到浏览器的url
        :return:
        """
        return self.driver.current_url

    def get_screenshot(self, file_path):
        """
        功能：截图并保存
        :param file_path:  文件路径
        :return:
        """
        self.driver.get_screenshot_as_file(file_path)

    def submit(self, element):
        """
        功能：提交特定的表单
        :param element:   元素表达式
        :return:
        """
        self.wait_element(element)
        self.find_element(element).submit()

    def switch_to_frame(self, element):
        """
        功能：切换到特定的frame
        :param element: 元素的表达式
        :return:
        """
        self.wait_element(element)
        self.driver._switch_to_frame(self.find_element(element))

    def switch_to_frame_out(self):
        """
        功能：切换道默认的上下文
        :return:
        """
        self.driver.switch_to.default_content()

    def F5(self):
        '''
        功能：刷新页面
        :return:
        '''
        self.driver.refresh()

    def accept_alert(self):
        """
        功能：确认按钮
        :return:
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        功能：对话框取消
        :return:
        """
        self.driver.switch_to.alert.dismiss()