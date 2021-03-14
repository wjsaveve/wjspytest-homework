# -*- coding: utf-8 -*-

from requestHttp.req_page.base import Base


class ContactBySession(Base):
    def create_number(self, mycode):
        myurl = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        myjson = {}
        myjson["userid"] = mycode
        myjson["name"] = "王" + mycode
        myjson["email"] = mycode + "@163.com"
        myjson["department"] = [1]
        r = self.s.post(url=myurl, json=myjson)
        # print(r.json())
        return r.json()

    def get_member(self, myuserid):
        myparm = {"userid": myuserid}
        r = self.s.get('https://qyapi.weixin.qq.com/cgi-bin/user/get', params=myparm)
        return r.json()

    def update_member(self, mycode):
        myurl = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        myjson = {}
        myjson["userid"] = mycode
        myjson["name"] = "王" + mycode + "_new"
        r = self.s.post(url=myurl, json=myjson)
        return r.json()

    def delete_member(self, myuserid):
        myparm = {"userid": myuserid}
        r = self.s.get('https://qyapi.weixin.qq.com/cgi-bin/user/delete', params=myparm)
        return r.json()
