#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'hlk'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from divconfig import setting
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml

testYaml = getyaml(setting.TEST_Element_YAML + '/' + 'intologin.yaml')

class IntoLogin(Page):
    """
    用户登录页面
    """
    url = '/home/'
    yzj_login_button_loc = (By.XPATH, testYaml.get_elementinfo(0))

    def into_login(self):
        """
        进入登录页
        :return:
        """
        self.find_element(*self.yzj_login_button_loc).click()

    # 切换账号密码登录
    switch_phone_loc = (By.XPATH, testYaml.get_elementinfo(1))

    def switch_phone(self):
        """
        切换账号密码登录
        """
        self.find_element(*self.switch_phone_loc).click()
        # sleep(1)

    def into_switch_login(self):
        """
        进入登录页，并切换账号密码登录
        """
        self.open()
        self.into_login()
        self.switch_phone()

    into_login_success_loc = (By.XPATH, testYaml.get_CheckElementinfo(0))

    # 登录异常情况提示
    # def into_login_error_hint(self):
    #     return self.find_element(*self.phone_pawd_error_hint_loc).text

    # 进入账号密码成功提示
    def into_login_success_hint(self):
        return self.find_element(*self.into_login_success_loc).text