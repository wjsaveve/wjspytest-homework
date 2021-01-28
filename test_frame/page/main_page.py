# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from test_frame.base_page import BasePage
from test_frame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        self.find_and_click(MobileBy.XPATH,
                            "//android.widget.TextView[@text='行情']")
        return MarketPage(self.driver)
