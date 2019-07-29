__author__ = 'nfdwadministrator_09'
import re
import os
import requests


indexurl = ('https://dmmtor.com/search/6381/')
indexur2 = ('https://dmmtor.com/')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
#url1 = str(url)+str(i)+'.html'
pname = requests.get (indexurl,headers = headers)
html = pname.text
patterns = re.compile('<a class="movie-box" href="/(.*?)">')
result = re.findall(patterns,html)
print (result)
for url1 in result:
        url2 = str(indexur2)+str(url1)
        print (url2)
        pname1 = requests.get (url2,headers = headers)
        html = pname1.text
        patterns = re.compile('<title>(.*?)</title>')
        result = re.findall(patterns,html)
        fname = str(result[0])+'.jpg'
        patterns1 = re.compile('<img src="(.*?)" title=".*?"></a>')
        result1 = re.findall(patterns1,html)
        print(result1)
        page = requests.get(str(result1[0]),headers = headers)
        file = open(fname,'wb')
        file.write(page.content)
        file.close()
        print ('已经下载完成'+str(fname))