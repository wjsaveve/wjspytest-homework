# -*- coding: utf-8 -*-
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestContact:
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = 'Android'
        desired_caps["deviceName"] = '127.0.0.1:7555'
        desired_caps["appPackage"] = "com.tencent.wework"
        desired_caps["appActivity"] = ".launch.WwMainActivity"
        desired_caps["noReset"] = True
        desired_caps["ensureWebviewsHavePages"] = True
        desired_caps['settings[waitForIdleTimeout]'] = 0  # 设置等待页面空闲的等待时间

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_adduser(self):
        codes = time.strftime("%m%d%H%M%S", time.localtime())
        name = "王健" + codes + "号"
        count = "wj" + codes
        phone = "180" + time.strftime("%m%d%M%S", time.localtime())
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable('
                                 'new UiSelector().scrollable(true).instance(0)'
                                 ').scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.TextView[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/..//android.widget.EditText[@text='必填']") \
            .send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.TextView[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.EditText[@text='手机号']") \
            .send_keys(phone)
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.TextView[@text='设置部门']").click()
        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[contains(@text,'确定')]").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.TextView[@text='保存']").click()
        time.sleep(5)

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
        assert "外出打卡成功" in self.driver.page_source
        time.sleep(5)
