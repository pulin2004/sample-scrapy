#!/usr/bin/python
#-*- coding: utf-8 -*-
import logging
import logging.config


logging.config.fileConfig('../logger.conf')
logger = logging.getLogger('stock')

def enum(**enums):
    return type('Enum', (), enums)

# Down 下降趋势，FLAT_DOWN 下降趋势，但开始走平，FLAT_FLAT 平直，FLAT_UP 走平，但成交量或价格缓慢上升，UP 上升趋势， HIGH 有见顶的可能
Numbers = enum(DOWN=10, DOWN_FLAT=20, FLAT_FLAT =30,UP_FLAT =40,UP=50,HIGH =60)

class Trend():
    def __init__(self, nextPoint,max_dif = 0.1 ,min_dif=0.05,boll_col = 1,close_col = 4):
        self._next = nextPoint
        self._max_dif = max_dif
        self._boll_col = boll_col
        self._close = close_col
        self._min_dif = min_dif

    def getTrendEnum(self, boll):
        pass

class DownTrend(Trend):

    def getTrendEnum(self, boll):
        _first = boll.getData()[0]
        _last = boll.getData()[-1]
        _firstValus = _first.getColumnAverage(self._boll_col)
        _lastValus = _last.getColumnAverage(self._boll_col)
        if float((_firstValus-_lastValus)/_lastValus) >=self._max_dif :
            boll.setMsg("下降振幅，开始%s-结束%s，超过%s"%(_firstValus,_lastValus,self._max_dif))
            return Numbers.DOWN
        else:
            _sec = boll.getHighSections();
            _mark = True
            for _data in boll.getData():
                if _data.isSection(_sec):
                    if (_data.getColumnAverage(self._boll_col) - _data.getColumnAverage(self._close))<0:
                        _mark = False
                        break
            if _mark:
                boll.setMsg("下降区间，开始%s-结束%s ,所有扩张区间是由下跌引起！" %(_firstValus, _lastValus))
                return Numbers.DOWN
            else:
                return self._next.getTrendEnum(boll)

class DownFlatTrend(Trend):

    def getTrendEnum(self, boll):
        _first = boll.getData()[0]
        _last = boll.getData()[-1]
        _firstValus = _first.getColumnAverage(self._boll_col)
        _lastValus = _last.getColumnAverage(self._boll_col)
        if float((_firstValus - _lastValus) / _lastValus) >= self._min_dif:
            _sec = boll.getHighSections();
            for _data in boll.getData():
                if _data.isSection(_sec):
                    if (_data.getColumnAverage(self._boll_col) - _data.getColumnAverage(self._close)) > 0:
                        _mark = True
                    else:
                        _mark = False
            if _mark:
                boll.setMsg("Down_Flat，开始%s-结束%s ,第一个扩张区间是由下跌引起！" %(_firstValus, _lastValus))
                return Numbers.DOWN_FLAT
            else:
                return self._next.getTrendEnum(boll)
        else:
            return self._next.getTrendEnum(boll)

class UpHighTrend(Trend):

    def getTrendEnum(self, boll):
        _first = boll.getData()[0]
        _last = boll.getData()[-1]
        _firstValus = _first.getColumnAverage(self._boll_col)
        _lastValus = _last.getColumnAverage(self._boll_col)
        if float((_lastValus-_firstValus)/_firstValus) >=self._max_dif :
            _sec = boll.getHighSections();
            _mark = True
            for _data in boll.getData():
                if _data.isSection(_sec):
                    if (_data.getColumnAverage(self._boll_col) - _data.getColumnAverage(self._close))>0:
                        _mark = False
                        break
            if _mark:
                boll.setMsg("上升通道，开始%s-结束%s ,所有扩张区间是由上涨引起！" %(_firstValus, _lastValus))
                return Numbers.UP
            else:
                boll.setMsg("上升通道,正在平台整理或筑顶！，开始%s-结束%s ,不是所有扩张区间是由上涨引起！" %(_firstValus, _lastValus))
                return Numbers.HIGH
        else:
            return self._next.getTrendEnum(boll)

class FlatUpTrend(Trend):

    def getTrendEnum(self, boll):
        _sec = boll.getHighSections();
        _mark = True
        for _data in boll.getData():
            if _data.isSection(_sec):
                if (_data.getColumnAverage(self._boll_col) - _data.getColumnAverage(self._close))>0:
                        _mark = False
                        break
        if _mark:
            boll.setMsg("平整阶段，准备开始上涨,所有扩张区间是由上涨引起！" )
            return Numbers.UP_FLAT
        else:
            boll.setMsg("平整阶段！,不是所有扩张区间是由上涨引起！" )
            return Numbers.FLAT_FLAT

class EndTrend(Trend):
    def __init__(self):
        pass

    def getTrendEnum(self, boll):
        logger.error("进入了错误的分支！")


def manageTrend():
    return DownTrend(DownFlatTrend(UpHighTrend(FlatUpTrend(EndTrend()))))

