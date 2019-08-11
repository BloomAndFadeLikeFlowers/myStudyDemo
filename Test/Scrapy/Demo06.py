# 使用Selenium爬取微信公众号文章
# 通过搜狗的微信搜索可以获取到微信公众号的文章

from bs4 import BeautifulSoup
import time
# 引入selenium和实例化一个Chrome浏览器引擎
from selenium import webdriver
driver = webdriver.Chrome(executable_path="F:\WebDriver\chromedriver.exe")

# 打开搜狗微信搜索
driver.get("http://weixin.sogou.com/")
# 定位到输入框
query = driver.find_element_by_id("query")
# 输入表单
query.send_keys("州的先生")
# 定位搜索按钮
search = driver.find_element_by_css_selector('input[value="搜公众号"]')
# 点击搜索按钮
search.click()
# 等待3秒
time.sleep(3)
# 定位搜索结果中的公众号，返回一个列表
gzh = driver.find_elements_by_xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[2]/p[1]/a')[0]
# 点击公众号
gzh.click()
# 等待3秒
time.sleep(3)
# 获取浏览器打开的窗口
handles = driver.window_handles
# 切换到新打开的窗口
driver.switch_to.window(handles[1])
# 保存页面为源码形式
page_source = driver.page_source
# 提取数据
soup = BeautifulSoup(page_source,"lxml")
title = soup.select("div.weui_media_box > div > h4")
subtitle = soup.select("div.weui_media_box > div > p.weui_media_desc")
pubtime = soup.select("div.weui_media_box > div > p.weui_media_extra_info")

for t,s,p in zip(title,subtitle,pubtime):
    print("标题：",t.get_text().replace("\n","").replace(" ",""))
    print("子标题：",s.get_text())
    print("时间：",p.get_text())
