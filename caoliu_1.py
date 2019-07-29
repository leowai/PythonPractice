__author__ = 'nfdwadministrator_09'
import re
import os
import requests

indexurl = ('https://dmmtor.com/')


url = ('https://dmmtor.com/d/105693/')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
#url1 = str(url)+str(i)+'.html'
pname = requests.get (url,headers = headers)
html = pname.text
patterns = re.compile('<title>(.*?)</title>')
result = re.findall(patterns,html)
fname = str(result[0])+'.jpg'
patterns1 = re.compile('<img src="(.*?)" title=".*?"></a>')
result1 = re.findall(patterns1,html)
page = requests.get(str(result1[0]),headers = headers)
file = open(fname,'wb')
file.write(page.content)
file.close()

