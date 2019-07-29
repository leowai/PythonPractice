__author__ = 'nfdwadministrator_09'
import os
import requests


headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '54.0.2840.98 Safari/537.36'
    }
url = ("https://pic.dmmtor.com/pic/CVDX-356/CVDX-356.jpg")
r=requests.get(url,headers = headers)
print(r.content)
file = open("pic.jpg",'wb')
file.write(r.content)
file.close()
print("图片保存cg")

#url = ("https://img.comicstatic.xyz/img/cn/855811/13.jpg")


#imgmax = 216
#imgmix = 1

# for imgurl in imgmax:
 #       print imgurl;

