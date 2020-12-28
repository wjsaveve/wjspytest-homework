import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


class TestSelenium():
    def setup(self):
        self.dr = webdriver.Chrome()
        self.dr.get("https://www.baidu.com")
        self.dr.maximize_window()

    def teardown(self):
        self.dr.quit()

    def test_se(self):
        self.dr.find_element(By.CSS_SELECTOR, "#kw").send_keys("我爱北京天安门")
        self.dr.find_element(By.XPATH, '//*[@id="su"]')
        sleep(5)

    def test_actionfun(self):
        self.dr.find_element(By.CSS_SELECTOR, "#kw").send_keys("我爱北京天安门")
        sleep(2)
        ele = self.dr.find_element(By.XPATH, '//*[@id="su"]')
        action = ActionChains(self.dr).click(ele)
        action.perform()
        sleep(3)
