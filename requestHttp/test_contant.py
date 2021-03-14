# -*- coding: utf-8 -*-
# 创建时间：2021/3/11 20:56
import pytest
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
        # myproxies = {"https": "127.0.0.1:7890"}
        # r = requests.get(myurl, proxies=myproxies, verify=False)
        r = requests.get(myurl)
        print(r.json())

    def test_updatemember(self):
        myurl = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.gettoken()}'
        myjson = {
            "userid": "Wang012601",
            "name": "王0311"
        }
        myproxies = {"https": "127.0.0.1:7890"}
        r = requests.post(url=myurl, json=myjson, proxies=myproxies, verify=False)
        print(r.json())

    @pytest.mark.parametrize("left,right", ([1, 6], [2, 9], [3.5, 8.2]))
    def test_generate(self, left, right, pre=1):
        result = []
        lefts = [left - pre, left, left + pre]
        rights = [right - pre, right, right + pre]
        mid = (left + right) / 2
        result += lefts
        result.append(mid)
        result += rights
        print(result)
        return result

    @pytest.mark.parametrize("mycode", ('wj03141701', 'wj03141702'))
    def test_create(self, mycode):
        myurl = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.gettoken()}'
        myjson = {}
        myjson["userid"] = mycode
        myjson["name"] = "王" + mycode
        myjson["email"] = mycode + "@163.com"
        myjson["department"] = [1]
        r = requests.post(url=myurl, json=myjson)
        print(r.json())
