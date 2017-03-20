#!/usr/bin/python
#-*- coding: utf-8 -*-

import csv
import os
import pandas as pd
import time
import numpy as np
import tushare as ts




class Stock_His():
    #整个目录应该是{$__base_path}/{random_code}/code.csv
    __base_path ="../../stock_his_data"
    def __init__(self,random_code,stock_code):
        self.__stock_code = stock_code
        self.__random_code = random_code
        pass

    def get_data(self):
        return os.path.join(self.__base_path ,self.__random_code,self.__stock_code+".cvs")

    def __load_his_data(self):
        path = self.__get_file_path()
        return pd.read_csv(path)

    def init_data(self,start,end = None,days= 10):
        df = ts.get_hist_data(self.__stock_code, start, end);
        df = df.sort_index()
        df1 = self.__get_max_values(df, ['close', 'high', 'volume'], days)
        df1 = df1.add_prefix("max_")
        df2 = self.__get_min_values(df, ['close', 'low','volume'], days)
        df2 = df2.add_prefix("min_")
        dfa = df1.merge(df2, left_index=True, right_index=True)
        dfb =df.merge(dfa,left_index=True, right_index=True)
        dfb.to_csv(self.__get_file_path())
        return dfb

    def __get_max_values(self,data,max_col,traday):
        _df = data.get(max_col)
        _adate = data.index.values
        _rdf = pd.DataFrame()
        for _index in range(len(_adate)):
            _df1=_df[_index:_index+traday]
            _s1 = _df1.max()
            _rdf[_adate[_index]] = _s1;
        return _rdf

    def __get_min_values(self,data,min_col,traday):
        _df = data.get(min_col)
        _adate = data.index.values
        _rdf = pd.DataFrame()
        for _index in range(len(_adate)):
            _df1 = _df[_index:_index + traday]
            _s1 = _df1.min()
            _rdf[_adate[_index]] = _s1;
        return _rdf



