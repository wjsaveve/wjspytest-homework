# -*- coding: utf-8 -*-
# 创建时间：2020/12/18 0:43
import pytest
import allure


@allure.feature("登录模块")
class TestLogin():

    @allure.testcase("http://www.baidu.com", "测试用例的链接")
    @allure.story("登录成功")
    def test_login_sucess(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登录页面"):
            print("打开登录页面")

        print("登录结果：这是登录成功")
        allure.attach("测试日志", "测试日志名称", attachment_type=allure.attachment_type.TEXT)
        allure.attach.file(
            "./img/testjpg.jpg", "日志图片",
            attachment_type=allure.attachment_type.JPG)
        assert 1 == 1

    @allure.story("登录失败-密码为空")
    def test_login_fail_null(self):
        print("登录结果：密码不能为空")
        assert 1 == 1

    @allure.story("登录失败-密码错误")
    def test_login_fail_erroe(self):
        print("登录结果：密码错误")
        assert 1 == 1

    @allure.story("登录失败-超时")
    def test_login_fail_outtime(self):
        print("登录结果：登录超时")
        assert 1 == 2
