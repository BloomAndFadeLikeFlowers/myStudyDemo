# Selenium 与 WebDriver 爬取数据

from bs4 import BeautifulSoup

# 引入selenium和实例化一个Chrome浏览器引擎
from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\WebDriver\chromedriver.exe")
# 打开一个网页
driver.get("http://www.baidu.com/")

# 元素定位

# 通过id属性定位
ele_id = driver.find_element_by_id("kw")
print(ele_id)

# 通过Xpath进行元素定位
ele_xpath = driver.find_element_by_xpath('//*[@id="kw"]')
print(ele_xpath)

# 通过标签名来定位元素
ele_labelname = driver.find_element_by_tag_name("input")
print(ele_labelname)

# 通过class类名来定位元素
ele_classname = driver.find_element_by_class_name("s_btn")
print(ele_classname)

# 保存页面代码供BeautifulSoup解析
driver.get("http://www.toutiao.com")
wbdata = driver.page_source
soup = BeautifulSoup(wbdata,"lxml")
img_news = soup.select("div.bui-left.index-content > div.bui-box.slide > ul.slide-list.bui-left > li > a")
for i in img_news:
    print(i.get_text())


