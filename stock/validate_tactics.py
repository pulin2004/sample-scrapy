#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import abstractmethod
import stock_date as stdate
import logging
import logging.config
import math

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('stock')

class Abstract_validate_tactics():

    #df 日期都是由近到远排序的Dataframe _row当前行 his_num 预计取计算得天数
    @abstractmethod
    def validate(self,df,_row,his_num,**b):
        pass



class Validate_days(Abstract_validate_tactics):
    def __init__(self, interval_days = 7):
        self.interval = interval_days

    def validate(self, df,_row, his_num, **b):
        if _row < his_num-1:
            return False
        else:
            if stdate.interval_days(df.ix[_row + 1- his_num  ,'date'],df.ix[_row,'date']) <= (self.interval+math.ceil(his_num/7.0)*2):
                return True;
            else:
                return False;


#每天收盘价低于开盘价，每天的最高价低于上一交易日的最高价，当前天收盘-开盘 大于 前几天 开盘到最高价 的1.8倍
class Validate_day_down(Abstract_validate_tactics):
    def __init__(self, multiple = 1.8):
        self.multiple = multiple

    def validate(self, df,_row, his_num, **b):
        if _row < his_num-1:
            return False
        else:
            _total=0.0
            _pre_high = 0.0
            for i in range(_row + 1- his_num ,_row):
                logger.debug("i is %s ,date is %s,high is %s ,open is %s ,close is %s"%(i,df.ix[i,'date'],df.ix[i,'high'],df.ix[i,'open'],df.ix[i,'close']))
                _total += df.ix[i,'high'] -df.ix[i,'open']
                if df.ix[i,'close'] > df.ix[i,'open']:
                    return False
                if i == _row + 1- his_num:
                    _pre_high=df.ix[i,'high']
                else:
                    if _pre_high < df.ix[i,'high']:
                        return False
            _zf = df.ix[_row,'close'] - df.ix[_row,'open']
            logger.debug("当日%s 涨幅： %s 累计 %s "%(df.ix[_row,'date'],_zf,_total))
            return _zf > (_total/(his_num-1))*self.multiple


