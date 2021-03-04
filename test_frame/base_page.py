# -*- coding: utf-8 -*-
import time

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_frame.adorner import balck_wrapper


class BasePage:
    def __init__(self, base_driver: WebDriver = None):
        self.driver = base_driver
        # self.black_list = BlackList().get_black_list()

    @balck_wrapper
    def find(self, mystype, myvalue=None):
        if myvalue is None:
            return self.driver.find_element(*mystype)
        else:
            return self.driver.find_element(by=mystype, value=myvalue)

    def find_and_click(self, mystype, myvalue=None):
        self.find(mystype, myvalue).click()

    def scroll_find(self, textValue):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable('
                                        'new UiSelector().scrollable(true).instance(0)'
                                        ').scrollIntoView(new UiSelector().'
                                        f'text("{textValue}").instance(0));')

    def finds(self, mystype, myvalue=None):
        if myvalue is None:
            return self.driver.find_elements(*mystype)
        else:
            return self.driver.find_elements(by=mystype, value=myvalue)

    def wait_for(self, locator, myvalue=None):
        if myvalue is None:
            return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(locator))
        else:
            return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(*locator))

    def quit(self):
        self.driver.quit()

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        print("当前Toast的信息为：" + result)
        return result

    def swip_find(self, by, locator):
        self.driver.implicitly_wait(1)
        eles = self.driver.find_elements(by, locator)
        while len(eles) == 0:
            self.driver.swipe(0, 600, 0, 400)
            eles = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)
        return eles[0]

    FIND = 'find'
    ACTION = 'action'
    FIND_AND_CLICK = 'find_and_click'
    SEND_KEYS = 'send_keys'
    VALYUE = 'value'

    def load_action(self, yaml_path):
        with open(yaml_path, encoding="UTF-8") as f:
            data = yaml.load(f)
        for step in data:
            xpath_expr = step.get(self.FIND)
            action = step.get(self.ACTION)
            set_value = step.get(self.VALYUE)
            if action == self.FIND_AND_CLICK:
                self.find_and_click(MobileBy.XPATH, xpath_expr)
            elif action == self.SEND_KEYS:
                self.find(MobileBy.XPATH, xpath_expr).send_keys(set_value)

    def screen_shot(self):
        codes = time.strftime("%m%d%H%M%S", time.localtime())
        img_path = "../image/" + codes + ".png"
        self.driver.save_screenshot(img_path)
        return img_path
