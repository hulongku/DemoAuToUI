#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'hlk'

from .driver import browser
import unittest
from selenium import webdriver


class MyTest(unittest.TestCase):
    """
    自定义MyTest类
    """
    dr = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        pass
        cls.driver = cls.dr
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.quit()