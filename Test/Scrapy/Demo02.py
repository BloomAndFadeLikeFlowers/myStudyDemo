#  第一个爬虫程序
#  爬取腾讯新闻上面的新闻

# 1.寻找数据特征 http://news.qq.com/

#  2.编写爬虫代码
import requests
from bs4 import BeautifulSoup

# 对腾讯新闻页面进行请求
url = "http://news.qq.com/"
wbdata = requests.get(url).text

# 对请求道的页面进行解析
soup = BeautifulSoup(wbdata,"lxml")
# select 选择器,选择新闻所在列表的标签
news_titles = soup.select("div.text > em.f14 > a.linkto")

for n in news_titles:
    # 提取标题和连接信息
    title = n.get_text()
    link = n.get("href")
    # 将提取到的信息拼成一个字典
    data = {
        "标题":title,
        "链接":link
    }
    print(data)


