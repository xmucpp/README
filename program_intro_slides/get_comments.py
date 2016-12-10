#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import re

def get_html(url):
    r = requests.get(url)
    #print r.encoding
    #print r.status_code
    #print r.content
    return r.content

def dispose_html(html):         #删除多余字段
    cut_html = re.findall("(?<=[(])[^()]+\.[^()]+(?=[)])",html)
    #print cut_html
    return cut_html[0]


def change_html(the_list):
    r = the_list.decode('GBK')  # unicode
    return json.loads(r)


def get_pagenumber():
    URL = 'https://sclub.jd.com/comment/productPageComments.action?productId=2680178&score=0&sortType=3&page=0&pageSize=10&callback=fetchJSON_comment98vv57476'
    html = get_html(URL)
    the_list = dispose_html(html)
    the_dict = change_html(the_list)
    return the_dict['maxPage']


def get_infor():
    comments = the_dict['comments']
    numbers = len(comments)
    for i in range(numbers):
        #print i
        print 'id:', comments[i]['id']
        print comments[i]['content']

a_ = get_pagenumber()
print a_
for i in range(a_):
    print i
    URL = 'https://sclub.jd.com/comment/productPageComments.action?productId=2680178&score=0&sortType=3&page=%d&pageSize=10&callback=fetchJSON_comment98vv57476'%i

    html = get_html(URL)
    the_list = dispose_html(html)
    the_dict = change_html(the_list)
    get_infor()