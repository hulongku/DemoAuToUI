#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys

from selenium.webdriver import ActionChains

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from divconfig import setting
from public.models import myunit,screenshot
from public.models.log import Log

from selenium import webdriver
import time

driver = webdriver.Chrome()
#打开百度
driver.get('https://kdtest.kdweibo.cn/home')
driver.maximize_window()
#设置隐式等待为5秒
# driver.implicitly_wait(20)
time.sleep(20)

# 搜索阿里巴巴
driver.find_element_by_xpath("//*[@id=\"headLogin\"]/a[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/div/div/h3/div[2]").click()
driver.find_element_by_id("email").send_keys("17200138001")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("log-btn").click()
driver.get('https://kdtest.kdweibo.cn/im/xiaoxi/')
time.sleep(3)
ActionChains(driver).move_to_element(driver.find_element_by_xpath("/html/body/header/div[2]/div/div[3]/ul/li[1]")).perform()
time.sleep(5)

# driver.find_element_by_id("kw").send_keys("阿里巴巴")
# driver.find_element_by_id("su").click()
# driver.find_element()
#等待5秒





# try:
#     f =open(setting.TEST_DATA_YAML + '/' + 'login_data.yaml',encoding='utf-8')
#     testData = yaml.load(f)
#     print(testData)
# except FileNotFoundError as file:
#     log = Log()
#     log.error("文件不存在：{0}".format(file))

