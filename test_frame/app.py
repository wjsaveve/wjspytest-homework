# -*- coding: utf-8 -*-
from appium import webdriver

from schoolTack_appium.PO.page.base_page import BasePage
from test_frame.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps["platformName"] = 'Android'
            desired_caps["deviceName"] = '127.0.0.1:7555'
            desired_caps["appPackage"] = "com.xueqiu.android"
            desired_caps["appActivity"] = ".common.MainActivity"
            desired_caps["noReset"] = True
            desired_caps["ensureWebviewsHavePages"] = True
            desired_caps['settings[waitForIdleTimeout]'] = 0  # 设置等待页面空闲的等待时间
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(5)

    def goto_main_page(self):
        return MainPage(self.driver)
