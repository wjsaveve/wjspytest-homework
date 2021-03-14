# -*- coding: utf-8 -*-
import requests
from requests import Session


class Base:
    def __init__(self):
        self.s = Session()
        self.corpid = 'ww8f606b7bdd404081'
        self.corpsecret = 'CDpNLlQTP6tAV6QCYxg91vMnW9HvuXwZCl9s2fX8ryA'
        self.s.params["access_token"] = self.gettoken().get("access_token")

    def gettoken(self, mycorpid=None, mycorpsecret=None):
        if mycorpid is None:
            mycorpid = self.corpid
        if mycorpsecret is None:
            mycorpsecret = self.corpsecret
        # 发送请求：写法一
        # myurl = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={mycorpid}&corpsecret={mycorpsecret}'
        # r = requests.get(myurl)
        # 发送请求：写法二
        myparm = {"corpid": mycorpid, "corpsecret": mycorpsecret}
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=myparm)
        # 获得全部返回值并json格式化
        # myjson = r.json()
        # 获得返回值中具体字段：写法一
        # mytoken = r.json()['access_token']
        # 获得返回值中具体字段：写法二
        # mytoken = r.json().get("access_token")
        return r.json()
