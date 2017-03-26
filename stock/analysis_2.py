#!/usr/bin/python
#-*- coding: utf-8 -*-

import numpy as np
import talib as ta
from stock_his import Stock_His
import logging
import logging.config
import matplotlib.pyplot as plt

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('stock')


def view_test():
    logger.info("start view_test test!")
    his = Stock_His("test",'600283')
    df = his.get_his_data()
    print df
    upperband, middleband, lowerband = ta.BBANDS(df['close'].values, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    print upperband
    print "-------------------"
    print middleband
    print "-------------------+++++++"
    print lowerband
    ig = plt.figure(1)
    plt.plot(upperband, color ='blue', linewidth = 1.0, linestyle =':',label='Straight-forward Structure')
    plt.plot(middleband, color ='green',linewidth=1.0, linestyle='-', label='Single-branch Structure')
    plt.plot(lowerband, color ='red', linewidth=1.0, linestyle='--',label='Double-branch Structure')
    plt.xticks(df['date'].values)
    plt.legend(loc='upper right')
    plt.title('SingleBranch(Blue) DoubleBranch(Green) TribleBranch(Red)')
    plt.show()
view_test()