#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import tushare as ts
import time

def get_max_values(data,max_col,traday):
    _df = data.get(max_col)
    _adate = data.index.values
    _rdf = pd.DataFrame()
    for _index in range(len(_adate)):
        _df1=_df[_index:_index+traday]
        _s1 = _df1.max()
        # print _adate[_index]+":"
        # print _s1
        _rdf[_adate[_index]] = _s1;
    return _rdf.T

def get_min_values(data,min_col,traday):
    _df = data.get(min_col)
    _adate = data.index.values
    _rdf = pd.DataFrame()
    for _index in range(len(_adate)):
        _df1=_df[_index:_index+traday]
        _s1 = _df1.min()
        # print _adate[_index]+":"
        # print _s1
        _rdf[_adate[_index]] = _s1;
    return _rdf.T

def get_single_stock_values(stock_code ,start_date,traday):
    df = ts.get_hist_data(stock_code, start_date);
    df = df.sort_index()
    df1 = get_max_values(df, ['close', 'open', 'high','low'], traday)
    df1 = df1.add_prefix("max_")
    df2 = get_min_values(df, ['close', 'open', 'ma5','low'], traday)
    df2 = df2.add_prefix("min_")
    dfa = df1.merge(df2, left_index=True, right_index=True)
    return dfa
print 'start --------'
_df_total = ts.get_stock_basics()
# _df_total =_df_total.head(40)
_d = dict()
_df_index =_df_total.index.values
for i in range(len(_df_index)):
    _code = _df_index[i]
    _d[_code]=get_single_stock_values(_code,'2017-01-01',10)
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"  " +_code+"  end!"
for k in dict:
    print "dict[%s] =" % k,dict[k]
print 'end --------'




