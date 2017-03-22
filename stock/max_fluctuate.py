#!/usr/bin/python
#-*- coding: utf-8 -*-

import pandas as pd
import logging
import logging.config
from stock_his import Stock_His
import validate_tactics
from stock_basic import Stock_Basic

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('stock')

class Validate_Max:

    def __init__(self, pre_num):
        self._pre_num = pre_num
        self.v1 = validate_tactics.Validate_days()
        self.v2 = validate_tactics.Validate_day_down()
        logger.debug("init  %s !" % (pre_num))

    def validate(self,df,current_num):
        if self.v1.validate(df,current_num,self._pre_num):
            if self.v2.validate(df,current_num,self._pre_num):
                return True
        return False


    def single_fileter(_self,_random,_code):
        logger.debug("start deal %s in %s !"%(_code,_random))
        _his = Stock_His(_random,_code)
        _rdf = pd.DataFrame()
        data = _his.get_his_data()
        data['stock_code'] =_code
        _t = len(data.index)
        for i in range(0, _t):
            logger.debug("start deal %s row (%s)" % (i, data.ix[i, 'date']))
            if _self.validate(data, i):
                logger.debug("%s row (%s) pass validate!" % (i, data.ix[i, 'date']))
                _serial = data.iloc[i]
                _rdf = _rdf.append(_serial)
        logger.debug("add row %s" % (_rdf.shape[0]))
        return _rdf


#测试
if __name__ == "__main__":
    logger.info("start max_fluctuate test!")
    _random ='test'
    _val = Validate_Max(5)
    _rdf = pd.DataFrame()
    _sb = Stock_Basic(_random)
    _sb_data = _sb.get_data()
    _t = len(_sb_data.index)
    for i in range(0,_t):
        _code = _sb_data.ix[i,'code']
        _df= _val.single_fileter(_random,_code)
        _rdf =_rdf.append(_df)
    _rdf.to_csv("./testdata/max_fluctuate.cvs")
    logger.info("end max_fluctuate test !")