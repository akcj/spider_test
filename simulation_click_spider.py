#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8') #gb2312,gbk

"""
    selenium+phantomjs模拟点击加载抓取豆瓣热门电影的名称和评分

Parameters:
  url - 抓取页面url
  more_xpath - xpath语法，查找到对应的更多按钮
Returns:
  返回登陆结果

"""
def simulation_click_spider(url,more_xpath):
    
    driver = webdriver.PhantomJS()
    driver.get(url)
    items = []
    i = 1
    while (driver.page_source.find(u'加载更多') != -1):
        
        print ('抓取第'+str(i)+'页').decode('utf-8')
        #数据过滤，匹配我们想要的数据
        soup = BeautifulSoup(driver.page_source,"lxml")
        values = soup.select('a[class="item"] > p ')
        
        for value in values:
            item = {}
            pattern = re.compile(r'<p>(.*?)<strong>', re.S)
            title = pattern.findall(str(value).decode('utf-8'))
            pattern = re.compile(r'<span.*?class="green">(.*?)</span>', re.S)
            title = pattern.sub('',str(title))
            title = title.replace("\\n", "").replace(" ", "")
            score = value.select('strong')[0].get_text()
            title = title[title.find('</span>')+7:].strip().decode('utf-8')
            item['score'] = score
            item['title'] = title
            if item not in items:
                items.append(item)
        try:        
            driver.find_element_by_xpath(more_xpath).click()
            i = i+1
            time.sleep(2)
        #点击失败，则直接提示错误，并中断抓取
        except:
            print ('抓取第'+str(i+1)+'页失败！').decode('utf-8')
            break
            
    print u'爬取完毕！'
    driver.quit()
    print items

if __name__ == '__main__':
    url = "https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=0"
    more_xpath = "//a[@class='more']"
    simulation_click_spider(url,more_xpath)