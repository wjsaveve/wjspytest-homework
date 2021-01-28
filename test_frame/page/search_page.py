# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from test_frame.base_page import BasePage


class SearchPage(BasePage):
    def opt_search(self):
        self.find(MobileBy.XPATH,
                  "//*[@resource-id='com.xueqiu.android:id/search_input_text']") \
            .send_keys("阿里巴巴")
        return True
