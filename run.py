# encoding:utf-8
import os
import time
 
import pytest
 
from common.send_email import Email
 
if __name__ == '__main__':
    pytest.main()
    time.sleep(2)
    os.system('allure generate temps -o ./reports --clean')
 
    #发送邮件
    #time.sleep(5)
    # e = Email()
    # report = "./reports/index.html"
    # e.send_email(report)
