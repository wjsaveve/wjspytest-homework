# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from schoolTack_appium.PO.page.base_page import BasePage
from schoolTack_appium.PO.page.manually_add_members_page import ManuallyAddMembersPage


class AddMemberMenuPage(BasePage):
    _location_add_member_manually = (MobileBy.XPATH,
                                     "//android.widget.TextView[@text='手动输入添加']")

    def goto_manually_add_members_page(self):
        self.find_and_click(self._location_add_member_manually)
        return ManuallyAddMembersPage(self.driver)
