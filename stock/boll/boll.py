#!/usr/bin/python
#-*- coding: utf-8 -*-

import numpy as np
import talib as ta
from region import Section
from region import Region
import logging
import logging.config
import matplotlib.pyplot as plt

logging.config.fileConfig('../logger.conf')
logger = logging.getLogger('stock')

class Boll():

    #num 集合分的数量
    def __init__(self,num =3):
        #boll.region 集合
        self.__data= None
        self.__num = num
        self.__sections =[]

    def calulateBoll(self,df, timeperiod=15,
                # number of non-biased standard deviations from the mean
                nbdevup=2,
                nbdevdn=2,
                # Moving average type: simple moving average here
                matype=0):
        upper, middle, lower = ta.BBANDS(df['close'].values,timeperiod,nbdevup,nbdevdn,matype)
        _sections = self.setSections(upper,middle)
        _max_line = len(middle) -1
        for i in range(0,_max_line):
            _stock = df.ix[i,]
            self.addDayValue(upper[i],middle[i],lower[i])

    def addDayValue(self,upper,middle,lower,open,close,volumn):
        if self.__data:
            _reg = self.__data[-1]
            if not _reg.add(upper, middle, lower, open, close, volumn):
                self.setDataRegion(middle, upper)
                self.addDayValue(upper, middle, lower, open, close, volumn)
            self.setDataRegion(middle, upper)
            self.addDayValue(upper,middle,lower,open,close,volumn)
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
        return None

    def getData(self):
        return self.__data

    def setSections(self,upper,middle):
        _u = np.array(upper)
        _m = np.array(middle)
        _dif = _u-_m
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


