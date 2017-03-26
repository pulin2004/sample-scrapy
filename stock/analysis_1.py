#!/usr/bin/python
#-*- coding: utf-8 -*-

from stock_basic import Stock_Basic
import pandas as pd
import logging
import logging.config


logging.config.fileConfig('logger.conf')
logger = logging.getLogger('stock')

def get_data():
    stock_base = Stock_Basic('test')
    df = stock_base.get_data()
    logger.info("stock base info %s,%s "%(df.shape[0],df.shape[1]))
    df1 = pd.read_csv("./testdata/max_fluctuate.cvs", dtype={'stock_code': str})
    logger.info("Data  info %s,%s "%(df1.shape[0],df1.shape[1]))
    return pd.merge(df1,df,how='left',left_on='stock_code',right_on= 'code',copy =True)


if __name__ == "__main__":
    logger.info("start analysis_1 test!")
    df = get_data()
    df1 = df[df.max_close>(df.close*1.1)]
    df1  = df1[['stock_code','date','open','high','close','max_high','min_low']]
    df1.to_csv("./testdata/max_fluctuate_1.cvs")
    print df1.shape
    df2 = df[df.close>(df.min_low*1.1)]
    df2 = df2[df2.low<>df2.min_low]
    df2 = df2[['stock_code', 'date', 'open', 'high', 'close', 'max_high', 'min_low','low']]
    df2.to_csv("./testdata/max_fluctuate_2.cvs")
    print df2.shape