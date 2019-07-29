
__author__ = 'Administrator'
import re
import requests
import pymysql


strarr = ['hellp','sfldkh','shitptptpp']
print (strarr)
    for b in range(0,2):
         #dv = strarr[b]
           db = pymysql.connect("localhost","root","yjgd@123","test",charset='utf8' )
     # 使用cursor()方法获取操作游标
         cursor = db.cursor()
    # 使用execute方法执行SQL语句
         sql ="INSERT INTO torld (title) VALUES ("+strarr[b]+")"
    #title =url1
         cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据
         db.commit()
    # 关闭数据库连接
         cursor.close()
         db.close()
         print (b)
   # print (strarr)
    #count = len(strarr)
   # print (count)共 75个元素
   # pri = strarr [0]
    #print （pri）
   # str1 = strarr[11]
   # print (str1)
