# 图片处理和ocr识别
import requests
import urllib.request
from bs4 import BeautifulSoup

# 设置headers头部
header = {
    "Host":"www.qqbiaoqing.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
    "Connection":"keep-alive",
    "Content-Type":"text/plain;Charset=UTF-8",
    "Accept-Language":"zh-cn",
    "Cookie":"BAIDUID=656731C425D07165C1513F063128DA68:FG=1;",
}

# 1. 图片保存与下载
# # 使用get请求获取图片链接
# imgdata = requests.get("https://www.qqbiaoqing.com/img/bd_logo1.png")
# print(imgdata.content)
#
# # 新建文件并写入相应内容
# with open("baidu.jpg","wb") as imgs:
#     imgs.write(imgdata.content)





# 表情包爬虫
url = "http://www.qqbiaoqing.com/bao/"

# 进行http请求
wbdata = requests.get(url,headers=header).content
soup = BeautifulSoup(wbdata,"lxml")

# 解析表情包连接
links = soup.select("div.item > div.ihd > a.title")
while True:
    for link in links:
        print(link)
        print(link.get("href"))
        # 请求表情包链接并获取表情图片原链接
        ldata = requests.get("http://www.qqbiaoqing.com" + link.get("href"),headers=header).content
        lsoup = BeautifulSoup(ldata,"lxml")
        imgsrc = lsoup.select("div.bd > ul.pics > li > a > img")
        for i in imgsrc:
            print(i.get("alt"))
            img = urllib.request.urlretrieve(i.get("src"),i.get("alt")+".gif")
