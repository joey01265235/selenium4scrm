#coding:utf-8

import unittest
import time

from scrmtest.AutomateDriver import AutomateDriver
from scrmtest.testcase.system_login import login

class test_scrm_login(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.baseurl = 'http://localhost:8080/index.html#'
        time.sleep(10)

    def testlogin(self):
        loginpage = login(self.driver,self.baseurl)
        loginpage.login('admin','123')
        time.sleep(2)
        self.assertEqual('http://localhost:8080/index.html#/',self.driver.getUrl())

    def tearDown(self):
        self.driver.quitBrowser()

if __name__ == '__main__':
    unittest.main()