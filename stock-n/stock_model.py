#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sqlalchemy import \
create_engine,Table,Column,Integer,String,MetaData,ForeignKey,Numeric
import db_config

engine=create_engine(db_config.DB_CONFIG,max_overflow=db_config.MAX_OVERFLOW)
metadata=MetaData(engine)

stock=Table('stock',metadata,
            Column('code',String(7),primary_key=True),
            Column('name',String(20)),
            Column('fullname',String(40)),
            Column('industry',String(100)),
            Column('area',String(20)),
            Column('pe',Integer),
            Column('outstanding',Numeric(10,2)),
            Column('totals',Numeric(10,2)),
            Column('total_assets',Numeric(10,2)),
            Column('liquid_assets',Numeric(10,2)),
            Column('fixed_assets',Numeric(10,2)),
            Column('reserved',Numeric(10,2)),
            Column('reserved_perShare',Numeric(5,2)),
            Column('eps',Numeric(5,2)),
            Column('bvps',Numeric(5,2)),
            Column('pb',Numeric(5,2)),
            Column('time_to_market',String(10)),
            Column('market',String(2))
           )

metadata.create_all()
