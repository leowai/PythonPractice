__author__ = 'Administrator'
import requests

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

#用get方法打开url并发送headers
#retry(tries=5,delay=5)

#conding = uft-8
url = "https://www.chiphell.com/portal.php?mod=list&catid=1"
r = requests.get(url,headers = header)
h = requests.post(url,headers = header)
sb = requests.encoding = 'uft-8'
de =requests.delete(url,headers = header)


print (sb)
print (h)
print (r.text)
print (r.status_code)