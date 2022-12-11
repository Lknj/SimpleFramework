# coding:utf-8
import requests
from common.logger import Log
 
 
class TestLogin:
 
    base_url = 'http://127.0.0.1:8888'
    headers = {
    'Accept': '*',
    'Accept-Encoding': '*',
    'Accept-Language': '*',
    'Connection': '*',
    'Content-Length': '*',
    'Content-Type': '*',
    'Cookie': '*',
    'I18N-Language': '*',
    'Sec-Fetch-Dest': '*',
    'Sec-Fetch-Mode': '*',
    'Sec-Fetch-Site': '*',
    'User-Agent': '*',
    'X-Requested-With': '*',
    }
    log = Log()
    def test_right_login(self):
        '''正确的用户名密码'''
        url = f'{self.base_url}/loginjosn'
        data = {
            'usrname':'123456',
            'pwd':'123456'
        }
        self.log.info('登陆成功')
        rep = requests.post(url,json=data)
        # print(rep.json())
        assert rep.json()['msg'] == '登陆成功'
 
    def test_falseusername_login(self):
        '''错误的用户名'''
        url = f'{self.base_url}/loginjosn'
        data = {
            'usrname':"xxx",
            'pwd':'xxx'
        }
        self.log.info('用户名或密码错误')
        rep = requests.post(url,json=data)
        #print(rep.json())
        if rep.json()['msg'] == '用户名或密码为空':
            assert rep.json()['msg'] == '用户名或密码为空'
        else:
            assert rep.json()['msg'] == '用户名或密码错误'
