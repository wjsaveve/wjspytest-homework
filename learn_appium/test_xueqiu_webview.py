# -*- coding: utf-8 -*-
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXuqiuWebview():
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True,
            # 'dontStopAppOnReset': True,
            'skipServerInstalltion': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            "chromedriverExecutable": r"C:\Users\WJ\Desktop\ccpx\chromedriver_win32(2.23-51~53)\chromedriver.exe"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_one(self):
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.RelativeLayout[3]").click()
        time.sleep(5)
