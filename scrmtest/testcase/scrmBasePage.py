class scrmBasePage(object):
    def __init__(self,driver,baseUrl):
        """
        构造方法
        :param driver: 封装好的driver
        :param baseUrl: 
        """
        self.driver = driver
        self.baseUrl = baseUrl

    def openPage(self,url):
        """
        打开页面，url拼接
        :param url: /sys/index.html
        :return: 
        """
        self.driver.navigate(self.baseUrl + url)