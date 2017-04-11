from scrmtest.testcase.scrmBasePage import scrmBasePage
from scrmtest.AutomateDriver import AutomateDriver

class login(scrmBasePage):
    location_accunt_input = 'x,//div/input[@placeholder="请输入帐号"]'
    location_password_input= 'x,//div/input[@type="password"]'
    location_capatch_input = 'x,//div/input[@placeholder="请输入验证码"]'
    location_login_button = 't,button'

    url = '/login'

    def __init__(self,driver,baseUrl):
        super().__init__(driver,baseUrl)

    def login(self,accunt,password):
        self.openPage(self.url)
        self.driver.implicitlyWait(3)
        self.driver.type(self.location_accunt_input,accunt)
        self.driver.type(self.location_password_input,password)
        self.driver.type(self.location_capatch_input,'520')
        self.driver.click(self.location_login_button)

