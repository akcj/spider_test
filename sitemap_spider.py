#-*- coding:utf-8 -*-

import urllib2
import re
"""
爬取网页html内容

Parameters:
  url - 要下载的url链接
  repeat_request_num - 重复请求次数，默认为2
  
Returns:
  返回网页html内容

"""
def download(url, repeat_request_num=2):
    print 'Downloading', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error', e.reason
        html = None 
        if repeat_request_num > 0:
            #判断错误值中code属性是否存在，并且错误code在500-600之间，则重复下载该url
            if hasattr(e,'code') and  500 <= e.code < 600:
                return download(url,repeat_request_num-1)
    return html


"""
sitemap爬虫

Parameters:
  sitemap_url - sitemap url链接

"""
def sitemap_spider(sitemap_url):
    sitemap = download(sitemap_url) #下载sitemap文件
    urls = re.findall('<loc>(.*?)</loc>',sitemap) #正则提取url
    for url in urls:
        html = download(url)

if __name__ == '__main__':
    url = 'https://www.xiuxiaowo.com/sitemap.xml'
    sitemap_spider(url)
