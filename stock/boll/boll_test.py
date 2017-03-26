#!/usr/bin/python
#-*- coding: utf-8 -*-

import boll
import unittest

class BollTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetSection(self):
        _boll = boll.Boll();
        _boll.setSections([3.3,1.8,3.2],[1,1.1,2])
        _sec1 = _boll.getSection(1.8,1.1)
        _sec2 =_boll.getSection(3.3,1)
        _sec3 =_boll.getSection(2.7,1)
        _sec4 = _boll.getSection(1.98,1)
        self.assertEqual(_sec1,_sec4)
        self.assertNotEqual(_sec1,_sec2)
        self.assertNotEqual(_sec2, _sec3)
        self.assertNotEqual(_sec1, _sec3)

    def testAddDayValue(self):
        _boll = boll.Boll()
        _boll.setSections([3.3,1.8,3.2],[1,1.1,2])
        _boll.addDayValue(3.3,1,0.8,3.2,3.3,99822)
        _boll.addDayValue(1.8,1.1,2,3.1,3,78923)
        _boll.addDayValue(2.7,1,1.4,2.4,2.5,28993)
        _boll.addDayValue(3.2, 1, 0.8, 3.2, 3.3, 94822)
        _data = _boll.getData();
        self.assertEqual(len(_data),4)

# 测试
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(BollTestCase("testGetSection"))
    suite.addTest(BollTestCase("testAddDayValue"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)