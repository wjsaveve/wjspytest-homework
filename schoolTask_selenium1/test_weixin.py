# -*- coding: utf-8 -*-
import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWexin:

    def teardown(self):
        self.dr.quit()

    def test_save_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        self.dr = webdriver.Chrome(options=opt)
        self.dr.implicitly_wait(5)
        self.dr.get("https://work.weixin.qq.com/wework_admin/frame")
        mycookie = self.dr.get_cookies()
        with open("cookie.yml", mode='w', encoding='UTF-8') as f:
            yaml.dump(mycookie, f)

    def test_adduser(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.implicitly_wait(5)
        # 打开浏览器，读取cookie信息进行登录。
        self.dr.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("cookie.yml", mode='r', encoding='UTF-8') as f:
            dates = yaml.safe_load(f)
            for date in dates:
                self.dr.add_cookie(date)
        self.dr.get("https://work.weixin.qq.com/wework_admin/frame")

        # 切换到通讯录页面，进行添加用户
        codes = time.strftime("%m%d%H%M%S", time.localtime())
        name = "王健" + codes + "号"
        count = "wj" + codes
        phone = "180" + time.strftime("%m%d%M%S", time.localtime())
        self.dr.find_element_by_id('menu_contacts').click()
        self.dr.find_element_by_link_text("添加成员").click()
        self.dr.find_element(By.ID, 'username').send_keys(name)
        self.dr.find_element(By.ID, "memberAdd_acctid").send_keys(count)
        self.dr.find_element(By.ID, "memberAdd_phone").send_keys(phone)
        self.dr.find_element_by_link_text("保存").click()
        time.sleep(2)
        resultnames = []
        eles = self.dr.find_elements(By.XPATH, '//*[@id="member_list"]/tr/td[2]')
        for ele in eles:
            resultnames.append(ele.get_attribute('title'))
        assert name in resultnames
