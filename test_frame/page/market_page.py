# -*- coding: utf-8 -*-

from test_frame.base_page import BasePage
from test_frame.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search_page(self):
        # self.find_and_click(MobileBy.XPATH,
        #                     "//android.widget.ImageButton[@resource-id='com.xueqiu.android:id/action_search']")
        self.load_action("../page/market_page.yaml")
        return SearchPage(self.driver)
