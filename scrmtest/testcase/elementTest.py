#coding:utf-8

import unittest

from scrmtest.AutomateDriver import AutomateDriver
from scrmtest.testcase.scrm_element import indexPage


class elementTest(unittest.TestCase):
    def setUp(self):
        self.autoDriver = AutomateDriver()
        self.baseUrl = 'http://localhost:8080/index.html#'

    def test_Element_guide(self):
        ''' 测试注释生成'''
        guidePage = indexPage(self.autoDriver,self.baseUrl)
        guidePage.openGuidePage()


if __name__ == "__main__":
    unittest.main()