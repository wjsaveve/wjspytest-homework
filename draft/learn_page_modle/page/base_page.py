# -*- coding: utf-8 -*-
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver=None):
        # 注解，不是赋值操作。用作ide的类型提示
        base_driver: WebDriver
        if base_driver is None:
            self.dr = webdriver.Chrome()
        else:
            self.dr = base_driver
        self.dr.implicitly_wait(3)
        self.dr.maximize_window()
