# -*- coding: utf-8 -*-
import allure

from test_frame.app import App


@allure.feature("搜索模块")
class TestCase:
    def setup_class(self):
        print("setup开始")
        self.app = App()

    def teardown_class(self):
        print("teardown结束")
        self.app.quit()

    @allure.testcase("http://www.baidu.com", "测试用例的链接")
    @allure.story("搜索成功")
    def test_search(self):
        self.app.start()
        self.app.goto_main_page().goto_market_page().goto_search_page().opt_search()
        allure.attach("测试日志内容", "测试日志标题", attachment_type=allure.attachment_type.TEXT)

    # @allure.testcase("http://www.baidu.com", "测试用例的链接2")
    # @allure.story("搜索成功")
    # def test_search2(self):
    #     self.app.start()
    #     self.app.goto_main_page().goto_market_page().goto_search_page().opt_search()
    #     allure.attach("测试日志内容", "测试日志标题", attachment_type=allure.attachment_type.TEXT)
