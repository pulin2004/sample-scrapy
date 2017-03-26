#!/usr/bin/python
#-*- coding: utf-8 -*-



def enum(**enums):
    return type('Enum', (), enums)

# Down 下降趋势，FLAT_DOWN 下降趋势，但开始走平，FLAT_FLAT 平直，FLAT_UP 走平，但成交量或价格缓慢上升，UP 上升趋势， HIGH 有见顶的可能
Numbers = enum(DOWN=10, FLAT_DOWN=20, FLAT_FLAT =30,FLAT_UP =40,UP=50,HIGH =60)

