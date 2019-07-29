__author__ = 'Administrator'
import requests
import re
from bs4 import BeautifulSoup

url = "https://sukebei.tordl.com/2.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
page = requests.get(url,headers = headers)
#page.encoding = 'gbk'
#soup = requests.get("https://sukebei.tordl.com/2.html")
#print (soup.text)
#print (page.text)
contents= page.text
patterns = re.compile('<a href=".*?" title="">(.*?)</a>',re.S)
#movieContent = re.findall('<a href=".*?" title="">(.*?)</a>',conent , re.S)
#pattern = re.compile('<br /><br />(.*?)<br /><br /><img')
#movieInfo = re.findall(pattern, movieContent[0])
#print (movieContent)
result = re.findall(patterns,contents)
print(result.group(2))