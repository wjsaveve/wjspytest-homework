# -*- coding: utf-8 -*-
from test_frame.app import App


class TestCase:
    def setup_class(self):
        print("setup开始")
        self.app = App()

    def teardown_class(self):
        print("teardown结束")
        self.app.quit()

    def test_add_member_byManually(self):
        self.app.start()
        self.app.goto_main_page().goto_market_page().goto_search_page().opt_search()
