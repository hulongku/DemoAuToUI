#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'hlk'

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest, ddt, yaml
from divconfig import setting
from public.models import myunit, screenshot
from public.page_obj.loginPage import Login
from public.models.log import Log
from time import sleep

try:
    f = open(setting.TEST_DATA_YAML + '/' + 'login_data.yaml', encoding='utf-8')
    testData = yaml.load(f)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))


@ddt.ddt
class Demo_UI(myunit.MyTest):
    """云之家登录测试"""

    def user_login_verify(self, phone, password):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :return:
        """
        Login(self.driver).user_login(phone, password)

    def phone_pwd_page(self):
        """
        进入手机号登录页
        """
        Login(self.driver).phone_pwd_page()

    def exit_login_check(self):
        """
        退出登录
        :return:
        """
        Login(self.driver).login_exit()

    @ddt.data(*testData)
    def test_login(self, datayaml):
        """
        登录测试
        :param datayaml: 加载login_data登录测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'], datayaml['detail']))

        self.user_login_verify(datayaml['data']['phone'], datayaml['data']['password'])

        po = Login(self.driver)
        if datayaml['screenshot'] == 'phone_pawd_success':
            sleep(3)
            log.info("检查点-> {0}".format(po.user_login_success_hint()))
            self.assertIn(datayaml['check'][0], po.user_login_success_hint(),
                          "成功登录，返回实际结果是->: {0}".format(po.user_login_success_hint()))
            log.info("成功登录，返回实际结果是->: {0}".format(po.user_login_success_hint()))
            screenshot.insert_img(self.driver, datayaml['screenshot'] + '.png')
            # log.info("-----> 开始执行退出流程操作")
            # self.exit_login_check()
            # po_exit = YZJlogin(self.driver)
            # log.info("检查点-> 找到{0}元素,表示退出成功！".format(po_exit.exit_login_success_hint()))
            # self.assertEqual(po_exit.exit_login_success_hint(), '登录',"退出登录，返回实际结果是->: {0}".format(po_exit.exit_login_success_hint()))
            # log.info("退出登录，返回实际结果是->: {0}".format(po_exit.exit_login_success_hint()))
        else:
            log.info("检查点-> {0}".format(po.phone_pawd_error_hint()))
            self.assertIn(datayaml['check'][0], po.phone_pawd_error_hint(),
                          "异常登录，返回实际结果是->: {0}".format(po.phone_pawd_error_hint()))
            log.info("异常登录，返回实际结果是->: {0}".format(po.phone_pawd_error_hint()))
            screenshot.insert_img(self.driver, datayaml['screenshot'] + '.png')


if __name__ == '__main__':
    unittest.main()
