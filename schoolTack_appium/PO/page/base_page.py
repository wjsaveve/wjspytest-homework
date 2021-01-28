# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, base_driver: WebDriver = None):
        self.driver = base_driver

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
