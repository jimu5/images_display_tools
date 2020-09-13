import os
from sql_tool.setting import database_setting
import pymysql

class DataLoader:
    def __init__(self):
        pass

    def connect_database(self):
        pass

    def create_table(self):
        pass

    def write_data(self):
        pass

    def get_file_pwd(self):
        pass
    
#连接数据库的ip，账号，密码，库名
db = pymysql.connect("localhost", "root", "b081db1aeae010f1", "images")
#创建游标
cursor = db.cursor()
#写入数据
sql = "insert into image_info(filename) values (%s)"
path = r'D:\资料\i\imgs' #所需要扫描文件夹的路径
i = 0 
for filename in os.listdir(path):
    print("写入第 " + str(i) + " 数据")
    cursor.execute(sql, (filename))
    i += 1
db.commit()
print("完成！")