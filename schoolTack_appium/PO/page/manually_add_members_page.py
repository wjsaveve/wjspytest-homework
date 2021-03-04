# -*- coding: utf-8 -*-
import time

from appium.webdriver.common.mobileby import MobileBy

from schoolTack_appium.PO.page.base_page import BasePage


class ManuallyAddMembersPage(BasePage):
    _location_input_name = (MobileBy.XPATH,
                            "//*[contains(@text,'姓名')]/..//android.widget.EditText[@text='必填']")
    _location_selectionBox_sex = (MobileBy.XPATH,
                                  "//*[contains(@text,'性别')]/..//*[@text='男']")
    _location_radio_sex_woman = (MobileBy.XPATH,
                                 "//android.widget.TextView[@text='女']")
    _location_input_phone = (MobileBy.XPATH,
                             "//android.widget.EditText[@text='手机号']")
    _location_button_depart = (MobileBy.XPATH,
                               "//android.widget.TextView[@text='设置部门']")
    _location_button_depart_set_ok = (MobileBy.XPATH, "//android.widget.TextView[contains(@text,'确定')]")
    _location_button_save = (MobileBy.XPATH,
                             "//android.widget.TextView[@text='保存']")

    def opt_add_member_nolyRequired(self):
        codes = time.strftime("%m%d%H%M%S", time.localtime())
        name = "王健" + codes + "号"
        phone = "180" + time.strftime("%m%d%M%S", time.localtime())
        self.find(self._location_input_name).send_keys(name)
        self.find_and_click(self._location_selectionBox_sex)
        self.wait_for(self._location_radio_sex_woman)
        self.find_and_click(self._location_radio_sex_woman)
        self.find(self._location_input_phone).send_keys(phone)
        self.find_and_click(self._location_button_depart)
        self.find_and_click(self._location_button_depart_set_ok)
        self.find_and_click(self._location_button_save)
        return self.get_toast_text()
