# -*- coding: utf-8 -*-
import time

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from simple_framework.basics.adorner import balck_wrapper


class BasePage:
    def __init__(self, base_driver=None):
        # 注解，不是赋值操作。用作ide的类型提示
        base_driver: WebDriver
        if base_driver is None:
            self.dr = webdriver.Chrome()
            self.dr.get("https://work.weixin.qq.com/wework_admin/frame")
            self.__cookie_login()
        else:
            self.dr = base_driver
        self.dr.maximize_window()
        self.dr.implicitly_wait(5)

    def __cookie_login(self):
        with open("cookie.yml", mode='r', encoding='UTF-8') as f:
            dates = yaml.safe_load(f)
            for date in dates:
                self.dr.add_cookie(date)
        self.dr.get("https://work.weixin.qq.com/wework_admin/frame")

    @balck_wrapper
    def find(self, mystype, myvalue=None):
        if myvalue is None:
            return self.dr.find_element(*mystype)
        else:
            return self.dr.find_element(by=mystype, value=myvalue)

    def finds(self, mystype, myvalue=None):
        if myvalue is None:
            return self.dr.find_elements(*mystype)
        else:
            return self.dr.find_elements(by=mystype, value=myvalue)

    def wait_click(self, locator, myvalue=None):
        if myvalue is None:
            return WebDriverWait(self.dr, 9).until(expected_conditions.element_to_be_clickable(*locator))
        else:
            return WebDriverWait(self.dr, 9).until(expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        self.dr.quit()

    def screen_shot(self):
        codes = time.strftime("%m%d%H%M%S", time.localtime())
        img_path = "../image/" + codes + ".png"
        self.dr.save_screenshot(img_path)
        return img_path
