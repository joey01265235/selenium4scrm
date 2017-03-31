#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select

class AutomateDriver(object):
    def __init__(self):
        driver = webdriver.Chrome()
        try:
            self.driver = driver
        except Exception:
            raise NameError('Chrome not find')

    def clearCookies(self):
        """
        driver init 后清除全部cookies
        :return: 
        """
        self.driver.delete_all_cookies()

    def refreshBrowser(self):
        """
        
        :return: 
        """
        self.driver.refresh()

    def maximizeWindow(self):
        """
        最大化窗口
        :return: 
        """
        self.driver.maximize_window()

    def navigate(self,url):
        """
        打开url
        :param url: 跳转/打开的地址
        :return: 
        """
        self.driver.get(url)

    def quitBrowser(self):
        """
        关闭浏览器
        :return: 
        """
        self.driver.close()


    def getElement(self,selector):
        """
        
        :param selector: 
        selector should be passed by an example with "id,xxx"
        :return: DOM element
        """
        if ',' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == "i" or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def type(self,selector,text):
        """
        操作输入框
        Usage:
        driver.type("id,el","selenium)
        :param selector: 
        :param text: 发送的文本
        :return: 
        """
        el = self.getElement(selector)
        el.clear()
        el.send_keys(text)

    def click(self,selector):
        """
        点击元素
        :return: 
        """
        el = self.getElement(selector)
        el.click()

    def selectByIndex(self,selector,index=0):
        """
        Usage:
        driver.select_by_index("i,el",0)
        :param selector: 
        :param index: 
        :return: 
        """
        el = self.getElement(selector)
        Select(el).select_by_index(index)

    def clickByText(self,text):
        self.getElement("")

    def submit(self,selector):
        """
        
        :param selector: 
        :return: 
        """
        el = self.getElement(selector)
        el.submit()

    def executeJs(self,script):
        """
        执行js脚本
        Usage:
        driver.js("window.scrollTo(200,1000);")
        :param selector: 
        :return: 
        """
        self.driver.execute_script(script)

    def getAttribute(self,selector,attribute):
        """
        Usage:
        driver.get_attribute("i,el","type")
        :param selector: 
        :param attribute: 
        :return: 
        """
        el = self.getElement(selector)
        return el.get_attribute(attribute)

    def getText(self,selector):
        """
        获取元素的文本信息
        Usage:
        driver.get_text("i,el")
        :param selector: 
        :return: 
        """
        el = self.getElement(selector)
        return el.text

    def isDisplay(self,selector):
        """
        Usage:
        driver.display("i,el")
        :param selector: 
        :return: 
        """
        el = self.getElement(selector)
        return el.is_displayed()

    def getTitle(self):
        return self.driver.title

    def getUrl(self):
        return self.driver.current_url

    def acceptAlert(self):
        self.driver.switch_to.alert.accept()

    def dismissAlert(self):
        self.driver.switch_to.alert.dismiss()

    def implicitlyWait(self,second=10):
        self.driver.implicitly_wait(second)

    def switchFrame(self,selector):
        """
        跳到指定的Frame
        :param selector: 
        :return: 
        """
        el = self.getElement(selector)
        self.driver.switch_to.frame(el)

    def switchDefaultFrame(self):
        self.driver.switch_to.default_content()

    def openNewWindow(self,selector):
        """
        在新窗口打开
        Usage:
        driver.open_new_window()
        :param selector: 
        :return: 
        """
        original_windows = self.driver.current_window_handle
        el = self.getElement(selector)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)

