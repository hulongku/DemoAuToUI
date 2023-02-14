#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'hlk'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from divconfig import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml

testyaml = getyaml(setting.TEST_Element_YAML + '/' + 'login.yaml')

class Login(Page):
    """
    用户登录页面
    """
    # url = '/home/'
    # yzj_login_button_loc = (By.XPATH, testyaml.get_elementinfo(0))

    # def yzj_login(self):
    #     """
    #     进入登录页
    #     :return:
    #     """
    #     self.find_element(*self.yzj_login_button_loc).click()

    # 定位器，通过元素属性定位元素对象
    # 切换账号密码登录
    # switch_phone_loc = (By.XPATH, testData.get_elementinfo(1))
    # 手机号输入框
    # login_phone_loc = (By.ID, testyaml.get_elementinfo(2))
    # # 密码输入框
    # login_password_loc = (By.ID, testyaml.get_elementinfo(3))
    # # 单击登录
    # login_user_loc = (By.ID, testyaml.get_elementinfo(4))
    # # 退出登录
    # login_exit_loc = (By.XPATH, testyaml.get_elementinfo(5))
    # # 选择退出
    # login_exit_button_loc = (By.XPATH, testyaml.get_elementinfo(6))

    # 手机号输入框
    login_phone_loc = (By.ID, testyaml.get_elementinfo(0))
    # 密码输入框
    login_password_loc = (By.ID, testyaml.get_elementinfo(1))
    # 单击登录
    login_user_loc = (By.ID, testyaml.get_elementinfo(2))
    # 退出登录
    login_exit_loc = (By.XPATH, testyaml.get_elementinfo(3))
    # 选择退出
    login_exit_button_loc = (By.XPATH, testyaml.get_elementinfo(4))

    def switch_phone(self):
        """
        切换账号密码登录
        :param username:
        :return:
        """
        self.find_element(*self.switch_phone_loc).click()
        # sleep(1)

    def login_phone(self, phone):
        """
        登录手机号
        :param username:
        :return:
        """
        # self.find_element(*self.login_phone_loc).clear()
        # self.find_element(*self.login_phone_loc).send_keys(phone)

        self.send_key(self.login_phone_loc, phone, True, False)

    def login_password(self, password):
        """
        登录密码
        :param password:
        :return:
        """
        # self.find_element(*self.login_password_loc).clear()
        # self.find_element(*self.login_password_loc).send_keys(password)

        self.send_key(self.login_password_loc, password, True, False)

    def login_button(self):
        """
        登录按钮
        :return:
        """
        self.find_element(*self.login_user_loc).click()

    def login_exit(self):
        """
        退出系统
        :return:
        """
        above = self.find_element(*self.login_exit_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        self.find_element(*self.login_exit_button_loc).click()

    def user_login(self, phone, password):
        """
        登录入口
        :param username: 用户名
        :param password: 密码
        :return:
        """
        # self.open()
        # self.yzj_login()
        # self.switch_phone()

        self.login_phone(phone)
        self.login_password(password)
        self.login_button()
        sleep(1)

    phone_pawd_error_hint_loc = (By.XPATH, testyaml.get_CheckElementinfo(0))
    user_login_success_loc = (By.XPATH, testyaml.get_CheckElementinfo(1))
    exit_login_success_loc = (By.XPATH, testyaml.get_CheckElementinfo(2))

    # 登录异常情况提示
    def phone_pawd_error_hint(self):
        return self.find_element(*self.phone_pawd_error_hint_loc).text

    # 登录成功用户名
    def user_login_success_hint(self):
        return self.find_element(*self.user_login_success_loc).text

    # 退出登录
    def exit_login_success_hint(self):
        return self.find_element(*self.exit_login_success_loc).text
