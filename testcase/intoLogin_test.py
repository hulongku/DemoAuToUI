#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'hlk'


import os,sys

from public.page_obj.intoLoginPage import IntoLogin

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from divconfig import setting
from public.models import myunit,screenshot
from public.page_obj.loginPage import Login
from public.models.log import Log
from time import sleep

try:
    f =open(setting.TEST_DATA_YAML + '/' + 'intologin_data.yaml', encoding='utf-8')
    testData = yaml.load(f)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))

@ddt.ddt
class Demo_UI(myunit.MyTest):
    """进入登录页测试"""
    def into_login(self):
        """
        进入登录页
        """
        IntoLogin(self.driver).into_switch_login()

    @ddt.data(*testData)
    def test_intologin(self, datayaml):
        """
        进入登录页
        :param datayaml: 加载intologin_data登录测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'], datayaml['detail']))

        self.into_login()

        po = IntoLogin(self.driver)
        if datayaml['screenshot'] == 'intologin_success':
            sleep(2)
            log.info("检查点-> {0}".format(po.into_login_success_hint()))
            self.assertIn(datayaml['check'][0], po.into_login_success_hint(), "进入账号密码登录页面成功，返回实际结果是->: {0}".format(po.into_login_success_hint()))
            log.info("进入账号密码登录页面成功，返回实际结果是->: {0}".format(po.into_login_success_hint()))
            screenshot.insert_img(self.driver, datayaml['screenshot'] + '.png')


if __name__ == '__main__':
    unittest.main()