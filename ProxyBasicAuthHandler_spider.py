#-*- coding:utf-8 -*-

import urllib2
"""
代理授权验证抓取网页html内容

Parameters:
  url - 要下载的url链接
  proxy_server - 私密代理IP地址
  username - 私密代理账号
  password - 私密代理密码
  repeat_request_num - 重复请求次数，默认为2
  
Returns:
  返回网页html内容
"""

def proxy_handler_spider(url, proxy_server, username, password, repeat_request_num=2):
    print 'Downloading', url
    try:
        #构建一个密码管理对象，用来保存需要处理的用户名和密码
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, proxy_server, username, password)
        proxy_auth_handler = rllib2.ProxyBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(proxy_auth_handler)
        request = urllib2.Request(url)
        response = opener.open(request)
        html = response.read()
        return html

    except urllib2.URLError as e:
        print 'Download error', e.reason
        html = None 
        if repeat_request_num > 0:
            #判断错误值中code属性是否存在，并且错误code在500-600之间，则重复下载该url
            if hasattr(e,'code') and  500 <= e.code < 600:
                return proxy_handler_spider(url, proxy_server, username, password, repeat_request_num-1)
        return html

if __name__ == '__main__':
    proxy_server = '192.168.0.1'
    username = 'username'
    password = 'password'
    url = "https://www.xiuxiaowo.com"
    print proxy_handler_spider(url, proxy_server, username, password)
