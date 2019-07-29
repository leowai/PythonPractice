'''

参考：http://www.jb51.net/article/82095.html

'''
import requests
from bs4 import BeautifulSoup  
import os
import re
import string
import xlsxwriter 
# 电影URL集合
movieUrls = []

# 获取电影列表
def queryMovieList(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
    page = requests.get(url,headers = headers)
    page.encoding = 'gbk'  
    html = page.text 
    pattern = re.compile ('<div class="title_all"><h1><font color=#008800>.*?</a>></font></h1></div>'+
                          '(.*?)<td height="25" align="center" bgcolor="#F4FAE2"> ',re.S)
    items = re.findall(pattern,html) 
    
    str = ''.join(items)
    pattern = re.compile ('<a href="(.*?)" class="ulink">(.*?)</a>.*?<td colspan.*?>(.*?)</td>',re.S)
    news = re.findall(pattern, str)
    for  j in news:
        movieUrls.append('http://www.dytt8.net'+j[0])

def queryMovieInfo(movieUrls):
    for index, item in enumerate(movieUrls):
        print('电影URL: ' + item)
        conent = requests.get(item)
        conent.encoding = 'gbk'  
        conent = conent.text
        movieContent = re.findall(r'<div class="co_content8">(.*?)</tbody>',conent , re.S)
        
        pattern = re.compile('<br /><br />(.*?)<br /><br /><img')
        movieInfo = re.findall(pattern, movieContent[0])

        if (len(movieInfo) > 0):
            movieInfo = movieInfo[0]+''
            # 删除<br />标签
            movieInfo = movieInfo.replace("<br />","")
            # 根据 ◎ 符号拆分
            movieInfo = movieInfo.split('◎')
        else:
            continue
        worksheet.write(index+1,0,movieInfo[1][5:])
        worksheet.write(index+1,1,movieInfo[2][5:])
        worksheet.write(index+1,2,movieInfo[3][5:])
        worksheet.write(index+1,3,movieInfo[4][5:])
        worksheet.write(index+1,4,movieInfo[5][5:])
        worksheet.write(index+1,5,movieInfo[6][5:])
        # 电影海报
        pattern = re.compile('<img.*? src="(.*?)".*? />', re.S)        
        movieImg = re.findall(pattern,movieContent[0])

        if (len(movieImg) > 0):
            movieImg = movieImg[0]
            worksheet.write(index+1,6,movieImg)
        else:
            movieImg = ""
 
        print("电影海报: " + movieImg)

        pattern = re.compile('<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">.*?</a></td>', re.S)
        movieDownUrl = re.findall(pattern,movieContent[0])

        if (len(movieDownUrl) > 0):
            movieDownUrl = movieDownUrl[0]
            worksheet.write(index+1,7,movieDownUrl)
        else:
            movieDownUrl = ""
        print("电影下载地址：" + movieDownUrl + "")
        print("------------------------------------------------\n\n\n")

if __name__=='__main__':
    
     workbook = xlsxwriter.Workbook('电影资源.xlsx')  
     worksheet = workbook.add_worksheet()
     worksheet.write(0,0,"译名")
     worksheet.write(0,1,"片名")
     worksheet.write(0,2,"年代")
     worksheet.write(0,3,"产地")
     worksheet.write(0,4,"类别")
     worksheet.write(0,5,"语言")
     worksheet.write(0,6,"海报链接")
     worksheet.write(0,7,"视频链接")
     print("开始抓取电影数据")
     for i in range(5):
         queryMovieList("http://www.dytt8.net/html/gndy/dyzz/list_23_" + str(i)+".html")
     print(len(movieUrls))
     queryMovieInfo(movieUrls)
     workbook.close() 
     print("结束抓取电影数据")
