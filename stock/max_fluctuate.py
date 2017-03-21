#!/usr/bin/python
#-*- coding: utf-8 -*-

import pandas as pd
import logging
import logging.config
from stock_his import Stock_His as sh
import validate_tactics

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('stock')

#测试
if __name__ == "__main__":
    logger.info("start stock_his test!")
    his = sh("test",'600283')
    data = his.get_his_data()
    _t = len(data.index)
    v1 = validate_tactics.Validate_days()
    v2 = validate_tactics.Validate_day_down()
    for i in range(0,_t):
        logger.debug("start deal %s row (%s)"%(i,data.ix[i,'date']))
        logger.debug("Validate_days is %s"%(v1.validate(data,i,5)))
        logger.debug("Validate_day_down is %s" % (v2.validate(data, i, 5)))