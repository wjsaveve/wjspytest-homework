# -*- coding: utf-8 -*-
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeiXinDaka():
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = 'Android'
        desired_caps["deviceName"] = '127.0.0.1:7555'
        desired_caps["appPackage"] = "com.tencent.wework"
        desired_caps["appActivity"] = ".launch.WwMainActivity"
        desired_caps["noReset"] = True
        desired_caps["ensureWebviewsHavePages"] = True
        caps['settings[waitForIdleTimeout]'] = 0  # 设置等待页面空闲的等待时间

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_one(self):
        time.sleep(5)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable('
                                 'new UiSelector().scrollable(true).instance(0)'
                                 ').scrollIntoView(new UiSelector().text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        time.sleep(5)
        assert "外出打卡成功" in self.driver.page_source()
        time.sleep(5)
