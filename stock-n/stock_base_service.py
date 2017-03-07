#!/usr/bin/env python
# -*- coding: utf-8 -*-


import stock_model as stock
import tushare as ts
from sqlalchemy.orm import sessionmaker


DB_Session = sessionmaker(bind=stock.engine)
session = DB_Session()

def update_stock_base():
    df = ts.get_stock_basics()
    print 'start -----'
    df.to_sql('stock',stock.engine,if_exists='replace')
    print 'end ------'


update_stock_base()

