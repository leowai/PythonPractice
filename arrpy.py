
__author__ = 'Administrator'
import re
import requests


strarr = []
print (strarr)
url = 'https://sukebei.tordl.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
for i in range (1,5196):
    url1 = str(url)+str(i)+'.html'
    page = requests.get(url1,headers = headers)
    #page.encoding = 'gbk'
    html = page.text
    patterns = re.compile('<a href=".*?" title="">(.*?)</a>')
    result = re.findall(patterns,html)
    #print(result)
    print("你正在打印第"+str(i)+"页")
    strarr = result
    for b in range(0,75):
         dv = strarr[b]
         print (dv)
   # print (strarr)
    #count = len(strarr)
   # print (count)共 75个元素
   # pri = strarr [0]
    #print （pri）
   # str1 = strarr[11]
   # print (str1)
