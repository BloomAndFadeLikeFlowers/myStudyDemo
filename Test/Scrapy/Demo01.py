# requests 模块
import requests
header = {
    "Host":"www.baidu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
    "Connection":"keep-alive",
    "Content-Type":"text/plain;Charset=UTF-8",
    "Accept-Language":"zh-cn",
    "Cookie":"BAIDUID=656731C425D07165C1513F063128DA68:FG=1;",
}
r_get = requests.get("http://www.aqsiq.gov.cn/zjxw/",headers=header)
r_get.encoding = "utf-8"
# for i in r_get.headers.items():
#     print(i)
# print(r_get.text)

from bs4 import BeautifulSoup
# f使用BeautifulSoup解析HTML
soup = BeautifulSoup(r_get.content,"lxml")
# 通过标签名获得数据
print(soup.title)
# 通过string属性获得标签中的数据
print(soup.title.string)
# 通过css选择器获取数据
items = soup.select("body > div.box.boxcenter > div.main > div.dc.fl_r.mar > div > div > ul > li > a[target='_blank']")
for i in items:
    print(i)
# 通过find方法获取数据
a_blank_one = soup.find("a",attrs={"target":"_blank"})
print(a_blank_one)
# r_post = requests.post("http://www.baidu.com")
# print(r_post)
