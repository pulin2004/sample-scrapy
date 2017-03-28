#!/usr/bin/python
#-*- coding: utf-8 -*-

import numpy as np
import talib as ta
from region import Section
from region import Region
import math
import logging
import logging.config
import matplotlib.pyplot as plt

logging.config.fileConfig('../logger.conf')
logger = logging.getLogger('stock')

class Boll():

    #num 集合分的数量
    def __init__(self,num =3):
        #boll.region 集合
        self.__data= []
        self.__num = num
        self.__sections =[]
        self.__msg =''

    def calulateBoll(self,df, timeperiod=15,
                # number of non-biased standard deviations from the mean
                nbdevup=2,
                nbdevdn=2,
                # Moving average type: simple moving average here
                matype=0):
        upper, middle, lower = ta.BBANDS(df['close'].values,timeperiod,nbdevup,nbdevdn,matype)
        self.setSections(upper,middle)
        _max_line = len(middle)
        for i in range(0,_max_line):
            _stock = df.ix[i,['open','close','volumn']]
            self.addDayValue(upper[i],middle[i],lower[i],_stock['open'],_stock['close'],_stock['volumn'])

    def addDayValue(self,upper,middle,lower,open,close,volumn):
        if not math.isnan(middle):
            if self.__data:
                _reg = self.__data[-1]
                if not _reg.add(upper, middle, lower, open, close, volumn):
                    self.setDataRegion(middle, upper)
                    self.addDayValue(upper, middle, lower, open, close, volumn)
                # self.setDataRegion(middle, upper)
                # self.addDayValue(upper,middle,lower,open,close,volumn)
            else:
                self.setDataRegion(middle, upper)
                self.addDayValue(upper,middle,lower,open,close,volumn)

    def setDataRegion(self, middle, upper):
        _sec = self.getSection(upper, middle)
        _reg = Region(_sec)
        self.__data.append(_reg)

    def getSection(self,upper,middle):
        for _sec in self.__sections:
            if _sec.inSection(upper - middle):
                return _sec
        logger.error("没有找到对应的section upper =%s , middle =%s"%(upper,middle))
        return None

    def getData(self):
        return self.__data

    def getHighSections(self):
        return self.__sections[-1]

    def setSections(self,upper,middle):
        _dif = self.__getUnit(upper,middle)
        _max = max(_dif)
        _min = min(_dif)
        _unit =(_max -_min)/self.__num
        self.__sections =[];
        for i in range(0,self.__num):
            if i == self.__num -1:
                _high = _max
            else:
                _high =_min+_unit
            self.__sections.append(Section(_min,_high))
            _min = _high

    def __getUnit(self,upper,middle):
        _dif = []
        for i in range(0,len(middle)):
            if not math.isnan(middle[i]):
                _dif.append(upper[i] - middle[i])
        return _dif

    def setMsg(self,msg):
        self.__msg = self.__msg+msg+" --,-- "

    def getMsg(self):
        return self.__msg
# 测试
if __name__ == "__main__":
    logger.debug("start Boll()")
    import tushare as ts
    import trend_strategy
    df = ts.get_hist_data('300321','2016-12-01')
    df = df.sort_index()
    # print df
    _boll = Boll()
    _boll.calulateBoll(df)
    _rf = trend_strategy.manageTrend().getTrendEnum(_boll)
    print _boll.getMsg()
    print _rf