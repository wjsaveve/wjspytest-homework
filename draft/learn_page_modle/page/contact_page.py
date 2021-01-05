# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from draft.learn_page_modle.page.base_page import BasePage


class ContactPage(BasePage):
    _location_listitem_name = (By.XPATH, '//*[@id="member_list"]/tr/td[2]')
    _location_button_adduser = (By.LINK_TEXT, '添加成员')
    _location_button_addmore = (By.CSS_SELECTOR, '.member_colLeft_top_addBtnWrap.js_create_dropdown')
    _location_button_adddepart = (By.CSS_SELECTOR, '.js_create_party')
    _location_input_depart_name = (By.CSS_SELECTOR, '[name="name"]')
    _location_input_depart_father = (By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list')
    _location_input_depart_father_listone = (
        By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688853110156868_anchor']")
    _location_button_depart_OK = (By.CSS_SELECTOR, '.qui_dialog_foot.ww_dialog_foot .qui_btn.ww_btn.ww_btn_Blue')
    _location_message_adddepart_pass = (By.ID, 'js_tips')

    def opt_getuser(self):
        '''
        获取成员列表，用来做断言
        :return:user_list，即用户列表（list格式）
        '''
        user_list = []
        # 加星号的意思是解元组，就是把元组拆成多个参数来使用
        eles = self.finds(*self._location_listitem_name)
        for ele in eles:
            user_list.append(ele.get_attribute('title'))
        return user_list

    def goto_AddUserPage(self):
        '''
        跳转到添加用户页面
        :return:AddUserPage类，即添加用户页面
        '''
        from draft.learn_page_modle.page.adduser_page import AddUserPage
        WebDriverWait(self.dr, 9).until(expected_conditions.element_to_be_clickable(self._location_button_adduser))
        self.find(*self._location_button_adduser).click()
        return AddUserPage(self.dr)

    def add_depart(self):
        '''
        在通讯录页面添加部门
        :return:
        '''
        codes = time.strftime("%m%d%H%M%S", time.localtime())
        name = "部门" + codes + "号"
        self.find(self._location_button_addmore).click()
        self.find(self._location_button_adddepart).click()
        self.find(self._location_input_depart_name).send_keys(name)
        self.find(self._location_input_depart_father).click()
        self.find(self._location_input_depart_father_listone).click()
        self.find(self._location_button_depart_OK).click()
        return self.find(self._location_message_adddepart_pass).text
