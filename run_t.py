import requests
url = 'http://127.0.0.1:8888/loginjosn'
data = {
    'username':'123456',
    'pwd':'123456'
}
rep = requests.post(url,json=data)
r = rep.json()['msg'] == '登陆成功'
print(r, rep.json())
# print(rep.text)