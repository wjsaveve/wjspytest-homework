# -*- coding: utf-8 -*-
from requestHttp.req_page.contact_bysession import ContactBySession


class TestContact:
    def setup_class(self):
        self.contact = ContactBySession()
        self.mycode = "wj03141834"

    def test_token(self):
        mytoken = self.contact.gettoken()
        print(mytoken)

    def test_creat(self):
        r = self.contact.create_number(self.mycode)
        print(r)

    def test_update(self):
        r = self.contact.update_member(self.mycode)
        print(r)

    def test_get(self):
        r = self.contact.get_member(self.mycode)
        print(r)

    def test_delete(self):
        r = self.contact.delete_member(self.mycode)
        print(r)
