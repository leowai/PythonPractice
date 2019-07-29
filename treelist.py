__author__ = 'Administrator'

import re
import requests
import pymysql
# 打开数据库连接
strarr = []


url = 'https://sukebei.tordl.com/'
headers =  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
for i in range (1,5196):
    url1 = str(url)+str(i)+'.html'
    page = requests.get(url1,headers = headers)
    #page.encoding = 'gbk'
    html = page.text
    patterns = re.compile('<a href=".*?" title="">(.*?)</a>')
    result = re.findall(patterns,html)
    strarr = result
    for b in range(0,75):
         dv = strarr[b]
         db = pymysql.connect("localhost","root","yjgd@123","test",charset='utf8' )
     # 使用cursor()方法获取操作游标
         cursor = db.cursor()
    # 使用execute方法执行SQL语句
         sql ="INSERT INTO torld (title) VALUES ("+strarr[10]+")"
    #title =url1
         cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据
         db.commit()
    # 关闭数据库连接
         cursor.close()
         db.close()
         print (str(strarr[b]))

 #  <a href=".*?" title="">(.*?)</a>.*?<a href="(.*?)">.*?<td class="text-center">(.*?)</td><td class="text-center">(.*?)</td>
 #  ('<a href=".*?" title="">(.*?)</a>')   正确的一条
 #('<a href=".*?" title="">(.*?)</a>.*?<a href="(.*?)">.*?<td class=".*?">(.*?)</td><td class=".*?">(.*?)</td>',re.S)
 #<a href="/s/a20fd45b66080a0df54b36da15da5a0b5f41c40c/" title="">[FHD] BCDP-084 素敵なカノジョ 向井藍 スレンダー美少女のコスプレおもらし中出し痙攣催眠せっくす</a>
#					</td>
##						<a href="/d/1554300282/a20fd45b66080a0df54b36da15da5a0b5f41c40c.torrent">
#							<i class="fa fa-fw fa-download"></i>
#						</a>
#						('<a href="(.*?)"><i class="fa fa-fw fa-magnet">')

# <a href="magnet:?xt=urn:btih:a20fd45b66080a0df54b36da15da5a0b5f41c40c">
#							<i class="fa fa-fw fa-magnet"></i>
#						</a>
#					</td>
#					<td class="text-center">8.5GB</td>
#                 ('<td class="text-center">(.*?)</td>')
#					<td class="text-center">2019-04-03 22:04</td>
