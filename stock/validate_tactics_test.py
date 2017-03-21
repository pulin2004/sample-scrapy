#!/usr/bin/python
#-*- coding: utf-8 -*-

from validate_tactics import Validate_day_down
import unittest
import pandas as pd

#执行测试的类
class ValidateTestCase(unittest.TestCase):
    def setUp(self):
        self.validate_day_down = Validate_day_down(2)
        self.df = pd.read_csv('./testdata/validate_tractics_test.cvs')

    def tearDown(self):
        self.validate_day_down = None
        self.df = None

    def testValidateTrue(self):
        self.assertTrue(self.validate_day_down.validate(self.df,4,5))
        self.assertFalse(self.validate_day_down.validate(self.df,3,5))
        self.assertFalse(self.validate_day_down.validate(self.df,5, 5))
        self.assertFalse(self.validate_day_down.validate(self.df, 10, 5))

#测试
if __name__ == "__main__":
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(ValidateTestCase("testValidateTrue"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
