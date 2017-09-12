#-*- coding:utf-8 -*-

import urllib2
import urllib
import ssl
"""
利用已登录的cookie信息登录网站

Parameters:
  url - 要下载的url链接
  cookie - 已经登录的cookie信息
  repeat_request_num - 重复请求次数，默认为2
  
Returns:
  返回网页html内容
"""

def cookie_spider(url, cookie, repeat_request_num=2):
    try:
        #关闭ssl证书验证，用户https的网站
        ssl._create_default_https_context = ssl._create_unverified_context
        
        #headers中的数据，可以通过抓包工具Fiddler获取
        headers = {
            "Host":"www.xiuxiaowo.com",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Cookie":cookie,
        }
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
        return response.read()

    except urllib2.URLError as e:
        print 'Download error', e.reason
        html = None 
        if repeat_request_num > 0:
            #判断错误值中code属性是否存在，并且错误code在500-600之间，则重复下载该url
            if hasattr(e,'code') and  500 <= e.code < 600:
                return cookie_spider(url, cookie, repeat_request_num-1)
    return html

if __name__ == '__main__':
    url = "https://www.xiuxiaowo.com/admin"
    cookie= "已经登录的cookie信息" 
    print cookie_spider(url,cookie)
