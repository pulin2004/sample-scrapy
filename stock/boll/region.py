#!/usr/bin/python
#-*- coding: utf-8 -*-

import numpy as np
import logging
import logging.config

logging.config.fileConfig('../logger.conf')
logger = logging.getLogger('stock')

class Region():

    def __init__(self,section):
        self.__section = section
        #第一位是upper，第二位是boll，第三位是lower，第四位是开盘价，第五位是收盘价，第六位是volume
        self.__data=[]

    def add(self,upper,boll,lower,open,close,vol):
        _dif = upper-boll
        if self.__section.inSection(_dif):
            self.__data.append([upper, boll, lower,open,close, vol])
            return True
        else:
            return False

    def getData(self):
        return self.__data

    def len(self):
        return self.__data.__len__()

class Section():

    def __init__(self, lowPoint,highPoint):
        self.__highPoint = highPoint
        self.__lowPoint = lowPoint

    def inSection(self,value):
        if value >= self.__lowPoint and value <= self.__highPoint:
            return True
        else:
            return False
# 测试
if __name__ == "__main__":
    logger.debug("start ")
    reg = Region(Section(5,4))
    reg.add(34.2,30.1,26.4,90000)
    logger.debug(reg.len())
