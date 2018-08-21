#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

import sys
from lxml import etree

import requests

from tkinter import *

user_id = 3877667526


def write_to_html_file(html_content):
    file_dir = os.path.split(os.path.realpath(__file__))[0] + os.sep + "weibo"
    if not os.path.isdir(file_dir):
        os.mkdir(file_dir)
    file_path = file_dir + os.sep + "%d" % user_id + ".html"
    f = open(file_path, "wb")
    f.write(html_content.encode(sys.stdout.encoding))
    f.close()
    print(u"微博写入文件完毕，保存路径:")
    print(file_path)


class Weibo:
    cookie = {
        "Cookie": "_T_WM=be77132bf44cce11cd210cbe564e616b; WEIBOCN_FROM=1110006030; SSOLoginState=1534390759; ALF=1536982759; SCF=AnnzUkj-MBJbwZ5cWKMGT968UJIB8DukUnLz7dKqnfCyTt6Yd29cQm5cNggoUncqY12KNBAsqe6189rnsPLgzgY.; SUB=_2A252cIG3DeRhGeBI6FoW9CnLzj-IHXVVmi__rDV6PUNbktANLUfNkW1NRp-UfHnKswIua2nfxv1R3k9iBwNCNuq4; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5JxPr-4Ynnija8BNTMMVgj5JpX5KMhUgL.Foqce0nNShMNSKe2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcSoeRS0BNS0-0; SUHB=0wn1cPVBNulhYJ; MLOGIN=1; M_WEIBOCN_PARAMS=fid%3D1005055030120112%26uicode%3D10000011"}  # 将your cookie替换成自己的cookie

    def __init__(self, profile_ftype, is_ori):
        self.user_id = user_id
        self.profile_ftype = profile_ftype
        self.username = ''
        self.weibo_content = []
        self.publish_time = []
        self.publish_tool = []

    def get_username(self):
        url = "https://weibo.com/u/%d?profile_ftype=1&is_ori=1#_0" % self.user_id
        html = requests.get(url, cookies=self.cookie)
        content = html.content
        result = etree.HTML(content)
        content_html = etree.tostring(result).decode('utf-8')
        # print(content_html)
        write_to_html_file(content_html)





def main():
    user_id = 3877667526
    profile_ftype = 1
    is_ori = 1
    wb = Weibo(profile_ftype, is_ori)
    wb.get_username()


if __name__ == '__main__':
    main()
