# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from schoolTack_appium.PO.page.address_book_page import AddressBookPage
from schoolTack_appium.PO.page.base_page import BasePage


class MessagePage(BasePage):
    _location_bottom_address = (MobileBy.XPATH,
                                "//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']")

    def goto_address_book_page(self):
        self.find_and_click(self._location_bottom_address)
        return AddressBookPage(self.driver)
