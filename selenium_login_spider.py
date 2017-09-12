#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("https://www.xiuxiaowo.com/admin")

# 输入账号密码
driver.find_element_by_name("username").send_keys("akcj_zl")
driver.find_element_by_name("password").send_keys("*****")
#模拟点击登录
driver.find_element_by_xpath("//input[@type='submit']").click()

time.sleep(3)
#生产快照
driver.save_screenshot("xiuxiaowo.png")
# with open("xiuxiaowo.html", "w") as file:
#     file.write(driver.page_source)
#关闭
driver.quit()

