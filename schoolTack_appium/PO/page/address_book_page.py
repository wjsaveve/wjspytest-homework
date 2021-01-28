# -*- coding: utf-8 -*-

from schoolTack_appium.PO.page.add_member_menu_page import AddMemberMenuPage
from schoolTack_appium.PO.page.base_page import BasePage


class AddressBookPage(BasePage):
    def goto_add_member_menu_page(self):
        self.scroll_find("添加成员").click()
        return AddMemberMenuPage(self.driver)
