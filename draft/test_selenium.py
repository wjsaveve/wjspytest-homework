import selenium
import time
import yaml
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

    def test_demo(self):
        self.dr.find_element(By.CSS_SELECTOR, "#kw").send_keys("霍格沃兹测试学院")
        self.dr.find_element(By.XPATH, '//*[@id="su"]').click()
        sleep(5)
        self.dr.find_element_by_xpath('//*[@id="1"]/h3/a').click()
        sleep(5)

        # 复用浏览器


class TestDemo2():
    def test_demo2(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        driver.find_element_by_id("menu_contacts").click()
        print(driver.get_cookies())

    # 使用cookie登录
    def test_cookie(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        cookies = [
            {'domain': '.qq.com', 'expiry': 1609408451, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853114004644'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853114004644'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1609494791, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1800860485.1609408331'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'QMvFnWsAx0cjL0AzvM-Cxfpg5idXx3vqWZh3lWBwQ4yGf8itLJgEetKhuFn39A_o'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a5103463'},
            {'domain': '.qq.com', 'expiry': 1920357252.139089, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '1_253478265'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1640944330, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1609408331'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'yC35-pi_vC6sjyqRZ6AHbLR3DvlabnZRX0L85YranyU5nesHjIhogKSDCkqEcGC3vB_HbgkV1CsTg4dvgnjbNCPUL6v5_hT0JZEUd2gcJ4LY8eA_9DnVhCQNlYyxlQtTagQLoe6tyGg3pQEMxowtnzZtr0zgAB3SEYSFVNVy4skV8CqovJOcWTGqTbQ-9RzAMY7pvdWPdIi8c9_VtlbOGUbEAEyZJ-a7T4A7NLXLRBFnywUZ1kzMmwfVlJq7v3GXp7AWQDjWQx6WCf7quT5-RA'},
            {'domain': '.qq.com', 'expiry': 1640662379.497207, 'httpOnly': True, 'name': 'pt2gguin', 'path': '/',
             'secure': False, 'value': 'o0253478265'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1609408331'},
            {'domain': '.qq.com', 'expiry': 1640662379.497147, 'httpOnly': True, 'name': 'ied_qq', 'path': '/',
             'secure': False, 'value': 'o0253478265'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '24419619393116401'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1609439843.274351, 'httpOnly': True, 'name': 'ww_rtkey',
             'path': '/', 'secure': False, 'value': '4r7v793'},
            {'domain': '.qq.com', 'expiry': 1920504379, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': 'b9de634d18305339'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1640944307.274442, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1612000391.472436, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1672480391, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.680073064.1609408331'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '1776384810'},
            {'domain': '.qq.com', 'expiry': 2147483643.613603, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
             'secure': False, 'value': '2b3490cb07c266c71eda6ff000bd7319405d49134d33bc68e1f6d20387d3032d'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': False, 'value': '253478265'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325082210115'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '4772951040'},
            {'domain': '.qq.com', 'expiry': 1920853204.808556, 'httpOnly': False, 'name': 'nutty_uuid', 'path': '/',
             'secure': False, 'value': 'd3955924-ecfb-4a21-8f05-d30d88e92fe9'},
            {'domain': '.qq.com', 'expiry': 1634867284, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': False, 'value': 'S1E6U0E3r3o3A1P238z4R598q2'},
            {'domain': '.qq.com', 'expiry': 2147483647.567454, 'httpOnly': False, 'name': 'RK', 'path': '/',
             'secure': False, 'value': '0SIhA5cnNQ'}]
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_id("menu_contacts").click()
        time.sleep(5)
        driver.quit()

    # 获取cookie，序列化后存入yaml文件内
    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = driver.get_cookies()
        print(cookie)
        with open("cookie.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)
