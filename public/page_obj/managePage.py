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

testYaml = getyaml(setting.TEST_Element_YAML + '/' + 'manage-web.yaml')


class Manage(Page):
    """
    用户登录页面
    """
    url = '/im/xiaoxi/'

    # 管理中心悬停区域
    manage_loc = (By.XPATH, testYaml.get_elementinfo(0))

    # 管理中心按钮
    manage_button_loc = (By.XPATH, testYaml.get_elementinfo(1))

    def yzj_manage(self):
        """
        进入管理中心
        :return:
        """
        self.open()
        # 鼠标悬停右上角
        self.move_to_element(self.find_element(*self.manage_loc))
        sleep(3)
        self.find_element(*self.manage_button_loc).click()
        sleep(3)

    # 管理中心eid元素控件
    manage_success_loc = (By.CLASS_NAME, testYaml.get_CheckElementinfo(0))

    # 进入成功校验
    def manage_success_hint(self):
        return self.find_element(*self.manage_success_loc).text
