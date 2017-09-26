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
    selenium+phantomjs模拟点击鼠标滑动

Parameters:
  url - 抓取页面url
  more_xpath - xpath语法，查找到对应的更多按钮
Returns:
  返回登陆结果

"""
def simulation_scroll_spider(url):
    
    driver = webdriver.PhantomJS()
    driver.get(url)
    driver.set_window_size(1440, 10000)
    js = "document.body.scrollTop=10000"
    driver.execute_script(js)
    time.sleep(10)
    driver.save_screenshot("weibo.png")

    driver.quit()

if __name__ == '__main__':
    url = "http://weibo.com/?category=0"
    simulation_scroll_spider(url)