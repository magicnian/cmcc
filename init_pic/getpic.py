#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import urllib
from urllib import request

import time

if __name__ == '__main__':

    for i in range(400, 3000):
        url = "http://shop.10086.cn/i/authImg?t=123"
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
            'Host': 'shop.10086.cn',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Cache-Control': 'no-cache'
        }

        request = urllib.request.Request(url, headers=header)
        response = urllib.request.urlopen(request).read()
        with open('E:\\爬虫资料\\移动图片验证码样本\\' + str(i) + '.png', 'wb') as f:
            f.write(response)

        time.sleep(1)
        i = i + 1
