#-*- coding:utf-8 -*-

import urllib2

"""
爬取网页html内容

Parameters:
  url - 要下载的url链接
  repeat_request_num - 重复请求次数，默认为2
  
Returns:
  返回网页html内容

"""

def opener_spider(url, repeat_request_num=2):
    print 'Downloading', url
    try:
        #构建一个HTTPHandler 处理器对象，支持处理HTTP请求
        #http_handler = urllib2.HTTPHandler()
        
        # 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
        http_handler = urllib2.HTTPSHandler()

        # 构建一个HTTPHSandler 处理器对象，支持处理HTTPS请求，同时开启Debug Log，debuglevel 值默认 0
        # 这样程序在执行的时候，会把收包和发包的报头在屏幕上自动打印出来，方便调试，有时可以省去抓包的工作。
        #http_handler = urllib2.HTTPSHandler(debuglevel=1)

        opener = urllib2.build_opener(http_handler)

        # 构建 Request请求
        request = urllib2.Request(url)
        # 调用自定义opener对象的open()方法，发送request请求
        response = opener.open(request)
        html = response.read()

    except urllib2.URLError as e:
        print 'Download error', e.reason
        html = None 
        if repeat_request_num > 0:
            #判断错误值中code属性是否存在，并且错误code在500-600之间，则重复下载该url
            if hasattr(e,'code') and  500 <= e.code < 600:
                return download(url,repeat_request_num-1)
    return html

if __name__ == '__main__':
    url = 'https://www.xiuxiaowo.com'
    print opener_spider(url)
