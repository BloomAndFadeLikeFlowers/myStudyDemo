#动态网站爬取  接口解析与Selenium

import requests
import json

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Connection':'keep-alive',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}
# 定义URL
url = "http://www.toutiao.com/api/pc/focus/"
# 请求URL
wbdata = requests.get(url,headers=header)
# 解析HTTP响应
news_title = json.loads(wbdata.text,encoding="utf-8")
print(news_title)
for n in news_title["data"]["pc_feed_focus"]:
    print(n["title"],n["display_url"],n["image_url"])
