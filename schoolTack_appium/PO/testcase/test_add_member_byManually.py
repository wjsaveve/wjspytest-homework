# -*- coding: utf-8 -*-
from schoolTack_appium.PO.page.app import App


class TestAddMemberByManually():
    def setup_class(self):
        print("setup开始")
        self.app = App()

    def teardown_class(self):
        print("teardown结束")
        self.app.quit()

    def test_add_member_byManually(self):
        self.app.start()
        self.app.goto_message_page() \
            .goto_address_book_page() \
            .goto_add_member_menu_page() \
            .goto_manually_add_members_page() \
            .opt_add_member_nolyRequired()
