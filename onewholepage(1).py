# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:28:28 2018

@author: user
"""

#coding=utf-8

import requests
from bs4 import BeautifulSoup
import os

import socket
import time

#from retry import retry

path='e:\\aga'


#f=open('i:\\yiyou.txt','r',encoding='utf-8')
#yiyou=f.read()
#f.close()

##这一段是改文件夹名称的
'''import os
path='i:\\aga\\'
files=os.listdir(path)
for i in files:
    oldname=i
    newname="".join(i.split())
    if newname!=oldname:
        os.rename(path+oldname,path+newname)
        print(newname)
'''
#标题里边有很多字符，无法创建文件夹，所以就把这些字符都替换为“1”
trantab=str.maketrans("|/\[]*:：><？?~，！!,","11111111111111111")
tranpic=str.maketrans("/\[]","1111")

###定义header，不知道具体有啥用
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

#用get方法打开url并发送headers
#retry(tries=5,delay=5)

for x in range(1,2): ### range是页面编号，这是最外层的循环。
    url='http://cl.r3y.xyz/thread0806.php?fid=16&search=&page='+str(x+1)#页面编号转化为字符，再跟网址一起，构成完整的地址
    print(url)  #调试用的
    #url = 'https://cl.unkbz.com/thread0806.php?fid=16&search=&page=6'
    
    #设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
    
    html = requests.get(url,headers = header) ##获取每一页的html
    #打印结果 .text是打印出文本信息即源码
    a=html.text.encode('iso-8859-1').decode('gbk') ### 先编码再解码，如果用默认的utf-8，都是乱码
    soup= BeautifulSoup(a,'html.parser') ### 用beautifulsoup进行解析？自己理解的
    b=soup.find_all('h3')  ### 获取页面当中每个帖子的链接，都是html语言的标志是<h3>
    totalurl=list() ###定义一个空列表，用来存储帖子地址
    for i in b:
        c=i.find('a').get('href') ### 用get函数，获取每个帖子的链接
        houzhui2=c.split('.')[-1] ###用来分理出后缀
        if houzhui2=='html':
            totalurl.append('http://cl.r3y.xyz/'+c) ###如果后缀是html的，就放进上面定义的列表
            
    for url_i in totalurl: ###第二个大循环，用来获取图片的链接
        html = requests.get(url_i,headers = header) ###先获取html
        #打印结果 .text是打印出文本信息即源码
        a=html.text.encode('iso-8859-1').decode('gbk')###同上
        soup= BeautifulSoup(a,'html.parser')### 同上
        file0=soup.head.title.string  ###获取帖子的标题，由于标题里边有很多无法命名文件夹的字符，所以要处理
        file1=file0.translate(trantab) ### 第一步处理掉“\”之类的
        if '達蓋爾的旗幟' in file1:  ###下面处理掉论坛标志
            file2=file1.replace(' - 達蓋爾的旗幟 1 草榴社區 - t66y.com','')
        elif ' - 達蓋爾的旗幟 1 草榴社區 - t66y.com' in file1:
            file2=file1.replace(' -  1 草榴社區 - t66y.com','')
        else:
            continue
        file="".join(file2.split()) ###去掉各种类型的空格。这里用了好多时间。
        if os.path.exists(path+'\\'+file)==True: ###判断路径下，是否有同名文件夹？ 如果有，就跳过。如果没有，就继续。
            print('already downloaded')
      
        else:
            print(file)  ###调试用的。
            os.makedirs(path+'\\'+file) ### 创建文件夹
            c=soup.find_all('input',attrs={"type": "image"}) ###提取图片的链接
            ##yiyou=yiyou+file+'**'
            if len(c)>0:
                for i in range(len(c)):###第三个循环，用来保存图片
                    print(i)###调试用的
                    picsrc=c[i].get('src')###获取图片的链接，html标志，有些是src，有些是data-src
                    if picsrc is None:
                        picsrc=c[i].get('data-src')
                    if '69img' in picsrc or 'freeimage' in picsrc or 'ultraimg' in picsrc or 'tumblr' in picsrc or '79img' in picsrc or 'x6img' in picsrc or 'sximg' in picsrc:
                        print('69img in picsrc')
                        break
                    else:
                    #houzhui=picsrc.split('.')[-1]
                    #time.sleep(sleep_download_time)
                        htmlpic = requests.get(picsrc,headers = header,timeout=500) ###获取图片内容，增加timeout，有些图片取不到就跳过。
        
                        filename=path+'\\'+file+'\\'+str(i)+'.'+'jpg' ###命名图片，地址+标题+图片数字
                        a=open(filename,'wb') ###以下为保存图片
                        a.write(htmlpic.content)
                        a.close
                        requests.Response.close(htmlpic)###这个一定要有，防止远程主机关闭（连接次数过多、过频繁，主机可能会认为是攻击）
                    time.sleep(10)

#f=open(path+'\\yiyou.txt','w',encoding='utf-8')
#f.write(yiyou)
#f.close()
print('本次下载完毕')
#break


