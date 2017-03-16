#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import tushare as ts

def get_max_values(data,max_col,traday):
    _df = data.get(max_col)
    _adate = data.index.values
    for _index in range(len(_adate)):
        _df1=_df[_index:_index+traday]
        _s1 = _df1.max()

