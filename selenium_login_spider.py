#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
"""
    selenium+phantomjs模拟登陆

Parameters:
  url - 登陆界面
  input_username_name - 用户名输入框的name属性值
  input_username_keys - 用户名
  input_password_name - 密码输入框的name属性值
  input_password_keys - 密码
  submit_xpath - xpath语法，查找到对应的登陆按钮
  
Returns:
  返回登陆结果

"""
def selenium_post_spider(url,input_username_name,input_username_keys,input_password_name,input_password_keys,submit_xpath):
    
    driver = webdriver.PhantomJS()
    driver.get(url)
    #找到用户框，并输入用户名
    try:
        driver.find_element_by_name(input_username_name).send_keys(input_username_keys)
    except:
        print 'username error!'
    #找到密码框，并输入密码
    try:
        driver.find_element_by_name(input_password_name).send_keys(input_password_keys)
    except:
        print 'password error!'
    #找到登陆按钮，并模拟点击
    try:
        driver.find_element_by_xpath(submit_xpath).click()
    except:
        print 'click error!'

    time.sleep(3)
    
    #当前页的url(登陆成功则为登陆页面)
    logined_url = driver.current_url
    #通过url变化判断是否登陆成功
    if(logined_url == url):
        print "login fail"
        driver.quit()
    else:
        print "login success"
        driver.quit()

if __name__ == '__main__':
    url = "https://www.xiuxiaowo.com/admin/login/?next=/admin/"
    input_username_name = "username" #输入框的name属性值
    input_username_keys = "your_username" 
    input_password_name = "password" #输入框的name属性值
    input_password_keys = "your_password"
    submit_xpath = "//input[@type='submit']"
    selenium_post_spider(url,input_username_name,input_username_keys,input_password_name,input_password_keys,submit_xpath)
