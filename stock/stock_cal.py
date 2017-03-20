#!/usr/bin/python
#-*- coding: utf-8 -*-

import stock_basic
import stock_his
import logging
import logging.config

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('stock')

def init_base_data(random_code,_date=None):
    _base = stock_basic.Stock_Basic(random_code)
    df = _base.init_data(_date)
    return df

def init_stock_data(random_code,_code,_days,_start,_end = None):
    logger.info("start deal %s !"%(_code))
    _his = stock_his.Stock_His(random_code,_code)
    return _his.init_data(_start,_days,_end)

if __name__ == "__main__":
    logger.info("start stock data prepare ！")
    random_code = "test"
    df = init_base_data(random_code)
    _df_index = df.index.values
    for i in range(len(_df_index)):
        _code = _df_index[i]
        _d1 = init_stock_data(random_code,_code,10,'2016-01-01')
    logger.info("complete stock data !")