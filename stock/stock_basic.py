#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import pandas as pd
import tushare as ts
import logging
import logging.config
import numpy as np

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('stock')

class Stock_Basic():
    # 整个目录应该是{$__base_path}/{random_code}/code.csv
    __base_path = "../../stock_his_data"

    def __init__(self, random_code):
        self.__random_code = random_code
        logger.debug("init  %s !" % (random_code))


    def __get_file_path(self):
        return os.path.join(self.__base_path, self.__random_code, "base_info.cvs")

    def __get_dir_path(self):
        return os.path.join(self.__base_path, self.__random_code)

    def get_data(self):
        path = self.__get_file_path()
        return pd.read_csv(path,dtype={'code':str})

    def init_data(self, date = None):
        df = ts.get_stock_basics(date)
        if not os.path.exists(self.__get_dir_path()):
            os.makedirs(self.__get_dir_path())
        df.to_csv(self.__get_file_path())
        return df


if __name__ == '__main__':
    logger.info("start stock_his test!")
    base = Stock_Basic("test")
    data = base.get_data()
    logger.debug(data['code'])

