#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
"""
    selenium+phantomjs模拟点击加载

Parameters:
  url - 登陆界面
  more_xpath - xpath语法，查找到对应的更多按钮
Returns:
  返回登陆结果

"""
def simulation_click_spider(url,more_xpath):
    
    driver = webdriver.PhantomJS()
    driver.get(url)
    while True:
        try:
            driver.find_element_by_xpath(more_xpath).click()
            time.sleep(2)
            print driver.current_url    
        except:
            print 'finished'
            break
    #关闭
    driver.quit()

if __name__ == '__main__':
    url = "https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
    more_xpath = "//a[@class='more']"
    simulation_click_spider(url,more_xpath)