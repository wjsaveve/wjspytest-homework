# -*- coding: utf-8 -*-

from test_frame.base_page import BasePage
from test_frame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        # self.find_and_click(MobileBy.XPATH,
        #                     "//android.widget.ImageView[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_and_click(MobileBy.XPATH,
        #                     "//android.widget.TextView[@text='行情']")
        self.load_action("../page/main_page.yaml")
        return MarketPage(self.driver)
