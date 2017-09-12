#-*- coding:utf-8 -*-

import urllib2
import random

"""
设置代理抓取网页html内容

Parameters:
  url - 要下载的url链接
  proxy_handler_set - 代理集合,默认为空（不设置代理）
  repeat_request_num - 重复请求次数，默认为2
  
Returns:
  返回网页html内容
"""

def proxy_handler_spider(url,proxy_handler_list=[],repeat_request_num=2):
    print 'Downloading', url
    try:
        if proxy_handler_list:
            proxy_one = random.choice(proxy_handler_list)
        else:
            proxy_one = {}
    
        proxy_handler = urllib2.ProxyHandler(proxy_one) #代理Handler，
        opener = urllib2.build_opener(proxy_handler)
        request = urllib2.Request(url)
        response = opener.open(request)
        html = response.read()

    except urllib2.URLError as e:
        print 'Download error', e.reason
        html = None 
        if repeat_request_num > 0:
            #判断错误值中code属性是否存在，并且错误code在500-600之间，则重复下载该url
            if hasattr(e,'code') and  500 <= e.code < 600:
                return proxy_handler_spider(url,proxy_handler_list,repeat_request_num-1)
        return html

if __name__ == '__main__':
    proxy_handler_list= [
            {'http':'123.7.38.31:9999'},
            {'http':'61.163.39.70:9999'},
            {'https':'218.29.111.106:9999'}
        ]
    url = "https://www.xiuxiaowo.com"
    print proxy_handler_spider(url,proxy_handler_list)
