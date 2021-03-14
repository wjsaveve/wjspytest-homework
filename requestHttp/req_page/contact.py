# -*- coding: utf-8 -*-
import requests


class Contact:
    def __init__(self):
        self.corpid = 'ww8f606b7bdd404081'
        self.corpsecret = 'CDpNLlQTP6tAV6QCYxg91vMnW9HvuXwZCl9s2fX8ryA'
        self.token = self.gettoken().get('access_token')

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

    def create_number(self, mycode):
        myparm = {"access_token": self.token}
        myurl = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        myjson = {}
        myjson["userid"] = mycode
        myjson["name"] = "王" + mycode
        myjson["email"] = mycode + "@163.com"
        myjson["department"] = [1]
        r = requests.post(url=myurl, json=myjson, params=myparm)
        # print(r.json())
        return r.json()

    def get_member(self, myuserid):
        myparm = {"access_token": self.token, "userid": myuserid}
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/get', params=myparm)
        return r.json()

    def update_member(self, mycode):
        myurl = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        myjson = {}
        myjson["userid"] = mycode
        myjson["name"] = "王" + mycode + "_new"
        r = requests.post(url=myurl, json=myjson)
        return r.json()

    def delete_member(self, myuserid):
        myparm = {"access_token": self.token, "userid": myuserid}
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/delete', params=myparm)
        return r.json()
