#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import tushare as ts

def get_max_values(data,max_col,traday):
    _df = data.get(max_col)
    _adate = data.index.values
    _rdf = pd.DataFrame()
    for _index in range(len(_adate)):
        _df1=_df[_index:_index+traday]
        _s1 = _df1.max()
        print _adate[_index]+":"
        print _s1
        _rdf[_adate[_index]] = _s1;
    return _rdf.T

def get_min_values(data,min_col,traday):
    _df = data.get(min_col)
    _adate = data.index.values
    _rdf = pd.DataFrame()
    for _index in range(len(_adate)):
        _df1=_df[_index:_index+traday]
        _s1 = _df1.min()
        print _adate[_index]+":"
        print _s1
        _rdf[_adate[_index]] = _s1;
    return _rdf.T

df = ts.get_hist_data('600231','2016-11-01');
df = df.head(20)
df = df.sort_index()
print df
print "------"
df1 = get_max_values(df,['close','open','ma5'],10)
df1 = df1.add_prefix("max_")
df2 = get_min_values(df,['close','open','ma5'],10)
df2= df2.add_prefix("min_")
dfa = df1.merge(df2,left_index = True,right_index=True)
print dfa