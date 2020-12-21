import selenium
import time
from selenium import webdriver


def test_se():
    dr = webdriver.Chrome()
    dr.get("https://www.baidu.com")
    time.sleep(5)
    dr.quit()
