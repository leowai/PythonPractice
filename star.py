__author__ = 'Administrator'
import requests,urllib
from bs4 import BeautifulSoup

ans = 0

for page in range(1,17):
     if page==1:
          url='http://www.gamersky.com/ent/201602/713895.shtml'
     else:
          url = 'http://www.gamersky.com/ent/201602/713895_'+str(page)+'.shtml'
     header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'}
     source_code = requests.get(url,headers = header)
     plain_text = source_code.text

     soup = BeautifulSoup(plain_text,"lxml")

     download_links = []
     folder_path = 'D://aa/'
     for pic_tag in soup.find_all('img'):
          pic_link = pic_tag.get('src')
          if pic_link.find('img1',7)!=-1:
               download_links.append(pic_link)

     for item in download_links:
         ans = ans+1
         urllib.urlretrieve(item,folder_path + item[-10:])
         print ('_',ans,'_个妹子已经静悄悄地躺在您的yin盘中')

