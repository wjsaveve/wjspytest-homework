# -*- coding: utf-8 -*-
import yaml
from selenium import webdriver


# 1、启动浏览器调试模式：
# 打开cmd对话框
# 切换到chrome所在的文件夹：如：cd C:\Users\WJ\AppData\Local\Google\Chrome\Application
# 然后执行命令：chrome --remote-debugging-port=9222
# 2、在打开的浏览器中，打开企业微信，扫码登录
# 3、执行下面的方法，保存cookie信息到yaml文件中

class TestSaveCookies:
    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        mycookie = driver.get_cookies()
        with open("cookie.yml", mode='w', encoding='UTF-8') as f:
            yaml.dump(mycookie, f)
            print("存储成功")
