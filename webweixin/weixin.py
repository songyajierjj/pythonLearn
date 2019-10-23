# -*- coding: utf-8 -*-
import json
import requests
from wxpy import *
# bot = Bot(cache_path=True) #通过缓存把登录信息保存下来不用每次都扫码登录

#给文件助手发消息
# bot.file_helper.send("hello")

# @bot.register()
# def print_message(msg):
#     print(msg.text)
#     return msg.text

# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    print("text="+text)
    url = "http://www.tuling123.com/openapi/api"
    api_key = "94152b80774b4837889d0e1d16914ccf"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "123456"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.text)
    return result["text"]

bot = Bot(console_qr=1, cache_path=True)

my_friend = bot.friends().search("老婆")[0]

my_group = bot.groups().search("金融科技中心（娱乐）")[0]


@bot.register(my_friend,my_group)
def forward_message(msg):
    print(msg.text)
    return auto_reply(msg.text)

embed()