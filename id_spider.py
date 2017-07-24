#-*- coding:utf-8 -*-

import urllib2
import re
import itertools
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
ID遍历爬虫

arameters:
  same_url - url的相同部分
  max_error - 最大错误次数

"""
def id_spider(same_url, max_error = 5):
    num_error = 0 #当前错误次数，初始为0
    for n in itertools.count(1): #itertools.count()创建一个无限的迭代器
        url = same_url + str(n)
        html = download(url)
        #错误5次，退出该爬虫
        if html is None:
            num_error += 1
            if num_error == max_error:
                break
        else:
            num_error = 0

if __name__ == '__main__':
    same_url = 'https://www.xiuxiaowo.com/article/'
    id_spider(same_url)