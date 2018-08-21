#!/usr/bin/env python
import tkinter

from tkinter import *
from tkinter.scrolledtext import ScrolledText

import requests
import json
import demjson
from json import JSONEncoder


class Application(Frame):
    container_id = 0

    def __init__(self):
        Frame.__init__(self, master=None)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.requestAPI = Button(self, text="get Cookie", command=self.requestAPI)
        self.requestAPI.pack()

    def requestAPI(self):
        # url = "https://m.weibo.cn/api/container/getIndex?uid=5575841531"
        username = "恋爱小事件"
        user_id = 3877667526
        container_id = self.requestContainerId(user_id, username)
        for index in range(3):
            weibo_list = self.requestWeiboList(container_id, user_id, username, index)
            print(weibo_list)
            # weibo_cards = json.loads(weibo_list)
            # print(weibo_cards['cards'])
            # stext = ScrolledText(bg='white', height=30)
            # stext.insert(END, weibo_list)
            # stext.pack(fill=BOTH, side=LEFT, expand=True)
            # stext.focus_set()

    def requestContainerId(self, userid, username):
        url = "https://m.weibo.cn/api/container/getIndex?q=%s&type=uid&value=%d" % (username, userid)
        # "&luicode=10000011&lfid=100103type=3&q=恋爱小事件&t=0&type=uid&value=5575841531&containerid=1076035575841531&page=2"
        result = requests.get(url)
        # my_json = content_str.decode('utf-8').replace("'", '"')
        # Load the JSON to a Python list & dump it back out as formatted JSON
        s = json.loads(result.text)
        jobj = s['data']['tabsInfo']['tabs']
        container_id = 0
        for tab in jobj:
            # print(tab)
            if tab['tab_type'] == "weibo":
                container_id = tab['containerid']
        # print("container_id: " + container_id)
        return container_id

    def requestWeiboList(self, container_id, userid, username, page):
        weibo_url = "https://m.weibo.cn/api/container/getIndex?q=%s&type=uid&value=%d&containerid=%d&page=%d" % (
            username, userid, int(container_id), page)
        print("weibo_url: " + weibo_url)
        weibo_result = requests.get(weibo_url)
        weibo_json = json.loads(weibo_result.text)
        weibo_list = json.dumps(weibo_json, indent=4, sort_keys=True)
        weibo_cards = json.loads(weibo_result.text)

        prettyWeiboList = ''
        # print("[")
        prettyWeiboList += "["
        for card in weibo_cards['data']['cards']:
            if 'mblog' in card:
                if 'pics' in card['mblog']:
                    prettyWeiboList += "{"
                    # print("{")
                    # print(card['mblog']['text'])
                    prettyWeiboList += "\"text\":" + "\"" + card['mblog']['text'] + "\","

                    # print()
                    prettyWeiboList += "\"pic\":" + "["
                    for pic in card['mblog']['pics']:
                        if 'large' in pic:
                            # print(pic['large']['url'])
                            prettyWeiboList += "\"" + pic['large']['url'] + "\","
                    prettyWeiboList += "]"
                    # print("},")
                    prettyWeiboList += "},"

            # print(card['mblog']['text'] + '\n')
            # print(card['mblog'])

        # print("]")
        prettyWeiboList += "]"

        # print(json.dumps(card, indent=4, sort_keys=True) + ",")
        print(weibo_list)
        # print(s1)
        return prettyWeiboList


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


class Encoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__()


class Weibo:
    def requestAPI(self):
        url = "https://m.weibo.cn/api/container/getIndex?uid=5575841531&luicode=10000011&lfid=100103type%3D3%26q%3D%E6%81%8B%E7%88%B1%E5%B0%8F%E4%BA%8B%E4%BB%B6%26t%3D0&type=uid&value=5575841531&containerid=1076035575841531&page=2"
        result = requests.get(url)
        content_str = result.content
        my_json = content_str.decode('utf-8').replace("'", '"')
        # print(my_json)

        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        # print(s)


def main():
    weiboApp = Application()
    # weiboApp.requestAPI()
    weiboApp.master.title("get json")
    weiboApp.mainloop()


main()
