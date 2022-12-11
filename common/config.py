# coding:utf-8
import pymysql
 
#定义一个类去数据库中查询
class DATABASE():
 
    def select_database(self):
        # 查询数据库
        # 打开数据库
        #数据库IP地址，用户名，密码，数据库
        db = pymysql.connect(host='localhost', user='root', password='mysql', database='***')
        # 使用cursor()方法创建一个游标对象cursor
        cursor = db.cursor()
 
        # 使用execute()方法执行sql查询，sql语句为你想要查询的
        cursor.execute('SELECT *** status = "***"')
 
        # 使用fetchone()方法获取单条数据
        # data = cursor.fetchone()
            
        Not_certified_company=''
 
        # 使用fetchall()方法获取所有数据，以元组形式返回
        try:
            data = cursor.fetchall()
            Not_certified_company = data[0][1]
        except Exception:
            print('')
       
        #关闭数据库
        db.close()
        #返回一个字段，主要是用于后面直接给用例一个参数
        return Not_certified_company
