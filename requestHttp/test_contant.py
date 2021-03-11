# -*- coding: utf-8 -*-
# 创建时间：2021/3/11 20:56
import requests


class TestContant:
    def gettoken(self):
        myurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8f606b7bdd404081&corpsecret=CDpNLlQTP6tAV6QCYxg91vMnW9HvuXwZCl9s2fX8ryA'
        r = requests.get(myurl)
        # print(r.json())
        mytoken = r.json()['access_token']
        return mytoken

    def test_getmember(self):
        myurl = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.gettoken()}&userid=WangJian'
        r = requests.get(myurl)
        print(r.json())

    def test_updatemember(self):
        myurl = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.gettoken()}'
        myjson = {
            "userid": "Wang012601",
            "name": "王0311"
        }
        r = requests.post(url=myurl, json=myjson)
        print(r.json())
