# -*- coding: utf-8 -*-
import time

from appium import webdriver


def test_one():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:7555',
        'appPackage': 'com.xueqiu.android',
        'appActivity': '.view.WelcomeActivityAlias',
        'noReset': True,
        'dontStopAppOnReset': True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    driver.implicitly_wait(5)
    driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("ceshi")
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]") \
        .click()
    time.sleep(5)
    driver.back()
    driver.quit()
