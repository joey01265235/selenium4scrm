from scrmtest.testcase.scrmBasePage import scrmBasePage

class indexPage(scrmBasePage):
    def __init__(self,driver,baseUrl):
        super().__init__(driver,baseUrl)
        self.mainPageUrl = '/#/zh-CN/component/installation'
        self.guidePageUrl = '/#/zh-CN/guide/design'
        self.driver.clearCookies()

    def openGuidePage(self):
        self.openPage(self.guidePageUrl)

