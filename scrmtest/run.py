import smtplib
import unittest
from email.header import Header
from email.mime.text import MIMEText

from scrmtest.HTMLTestRunner import HTMLTestRunner
from scrmtest.testcase.scrm_login_test import test_scrm_login


class scrmTestRunner():

    def runTest(self):
        """
        运行测试用例
        :return: 
        """
        #1.创建测试套件
        suilt = unittest.TestSuite()

        #2.添加测试用例
        suilt.addTest(test_scrm_login('testlogin'))

        #3.测试结果文件
        buf = open("./result.html","wb")

        #4.创建runner
        runner = HTMLTestRunner(stream=buf,title='Scrm Test Result',description='Test Case Run Result')

        runner.run(suilt)

        #5.关闭文件
        buf.close()

    def sendEmail(self,targetEmail):
        """
        发送邮件
        :param targetEmail: 
        :return: 
        """
        f = open("./result.html",'rb')

        mailBody = f.read()

        #申明邮件对象
        msg = MIMEText(mailBody,'html','utf-8')
        #邮件主题
        msg['subject'] = Header('scrm自动化测试结果','utf-8')
        msg['From'] = 'zhouyi<joey01265235@163.com>'
        # msg['To'] = '121903163@qq.com'
        msg['To'] = 'yi.zhou@kuailework.com'
        # msg['To'] = 'runfeng.cao@kuailework.com'

        #SMTP服务对象
        smtpMail = smtplib.SMTP()

        #连接SMTP服务器
        smtpMail.connect('smtp.163.com')

        #登录SMTP服务器
        smtpMail.login('joey01265235@163.com','zylovekll5051560')

        #使用SMTP服务器发送邮件
        smtpMail.sendmail('joey01265235@163.com',targetEmail,msg.as_string())

        smtpMail.quit()

if __name__ == '__main__':
    run = scrmTestRunner()
    run.runTest()
    run.sendEmail('yi.zhou@kuailework.com')