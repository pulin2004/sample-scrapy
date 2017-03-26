#!/usr/bin/python
#-*- coding: utf-8 -*-


import region
import unittest

class RegionTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInSection(self):
        _sec = region.Section(1.23,3.4)
        self.assertTrue(_sec.inSection(2))
        self.assertFalse(_sec.inSection(1.229999))
        self.assertFalse(_sec.inSection(3.400001))
        self.assertTrue(_sec.inSection(1.23))
        self.assertTrue(_sec.inSection(3.4))

    def testRegion(self):
        _sec = region.Section(0.05,0.15)
        _reg =region.Region(_sec)
        self.assertTrue(_reg.add(3.5,3.4,3.2,3.49,3.15,988232))
        self.assertTrue(_reg.add(3.48,3.33,3.1,3.46,3.16,899000))
        self.assertFalse(_reg.add(3.57,3.41,3.21,3.56,3.19,8923000))
        self.assertEqual(_reg.len(),2)
        self.assertListEqual(_reg.getData(),[[3.5,3.4,3.2,3.49,3.15,988232],[3.48,3.33,3.1,3.46,3.16,899000]])

# 测试
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(RegionTestCase("testInSection"))
    suite.addTest(RegionTestCase("testRegion"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)