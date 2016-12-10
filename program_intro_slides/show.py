#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import re
url ='https://sclub.jd.com/comment/productPageComments.action?productId=2680178&score=0&sortType=3&page=106&pageSize=10&callback=fetchJSON_comment98vv57476'
r = requests.get(url)
#print r.encoding
#print r.status_code
#r = r.content
#print r
#r = re.findall("(?<=[(])[^()]+\.[^()]+(?=[)])", r)  # 去除多余的部分，下两行代码用于转码
#print r
#r = r[0]
#print r
#r = r.decode('GBK')  # unicode
#r = json.loads(r)
#buyer_comment = r['comments']
#numbers = len(buyer_comment)
#for i in range(numbers):
    #print 'id:', buyer_comment[i]['id']
    #print buyer_comment[i]['content']