#!/usr/bin/python
#-*- coding: utf-8 -*-


import os
import pandas as pd
import tushare as ts
import logging
import logging.config

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('stock')

class Stock_His():
    #整个目录应该是{$__base_path}/{random_code}/code.csv
    __base_path ="../../stock_his_data"

    def __init__(self,random_code,stock_code):
        self.__stock_code = stock_code
        self.__random_code = random_code
        logger.debug("init %s stock His for %s !"%(stock_code,random_code))


    def __get_file_path(self):
        return os.path.join(self.__base_path ,self.__random_code,self.__stock_code+".cvs")

    def __get_dir_path(self):
        return os.path.join(self.__base_path ,self.__random_code)

    def get_his_data(self):
        path = self.__get_file_path()
        if os.path.exists(path):
            return pd.read_csv(path)
        else:
            logger.warn("%s No file!" % (path))
            return None

    def init_data(self,start,days= 10,end = None):
        logger.info("init_data %s in (%s - %s -----start!"%(self.__stock_code,start,end))
        df = ts.get_hist_data(self.__stock_code, start, end)
        if df:
            df = df.sort_index()
            df1 = self.__get_max_values(df, ['close', 'high', 'volume'], days)
            df1 = df1.add_prefix("max_")
            df2 = self.__get_min_values(df, ['close', 'low','volume'], days)
            df2 = df2.add_prefix("min_")
            dfa = df1.merge(df2, left_index=True, right_index=True)
            dfb =df.merge(dfa,left_index=True, right_index=True)
            # print dfb
            if not os.path.exists(self.__get_dir_path()):
                os.makedirs(self.__get_dir_path())
            dfb.to_csv(self.__get_file_path())
            logger.info("init_data %s in (%s - %s -----end!" %(self.__stock_code, start, end))
            return dfb
        else:
            logger.warn("%s No Data!"%(self.__stock_code))
            return None

    def __get_max_values(self,data,max_col,traday):
        _df = data.get(max_col)
        _adate = data.index.values
        _rdf = pd.DataFrame()
        for _index in range(len(_adate)):
            _df1=_df[_index:_index+traday]
            _s1 = _df1.max()
            _rdf[_adate[_index]] = _s1;
        return _rdf.T

    def __get_min_values(self,data,min_col,traday):
        _df = data.get(min_col)
        _adate = data.index.values
        _rdf = pd.DataFrame()
        for _index in range(len(_adate)):
            _df1 = _df[_index:_index + traday]
            _s1 = _df1.min()
            _rdf[_adate[_index]] = _s1;
        return _rdf.T


if __name__ == '__main__':
    logger.info("start stock_his test!")
    his = Stock_His("test",'603041')
    his.init_data("2016-01-01")
    data = his.get_his_data()
    logger.debug(data)
