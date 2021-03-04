# -*- coding: utf-8 -*-
from appium import webdriver


class TestAppiumWeb():
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'paltformVersion': '6.0',
            'browserName': 'Browser',
            'noReset': True,
            'skipServerInstalltion': True,
            # 'deviceName': '127.0.0.1:7555',
            'deviceName': '3dcddf0a',
            "chromedriverExecutable": r"E:\ccpx\chromedriver_win32_71.0.3578.33\chromedriver.exe"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_one(self):
        self.driver.get("https://m.baidu.com")
        # self.driver.find_element(MobileBy.ID, "index-kw").send_keys("my love ling")
        # WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((MobileBy.ID, 'index-bn')))
        # self.driver.find_element(MobileBy.ID, 'index-bn').click()
