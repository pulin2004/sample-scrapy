#!/usr/bin/python
#-*- coding: utf-8 -*-

import datetime


def get_day():
    _date = datetime.datetime.now()
    return to_str(_date)

def add(day,num):
    _day = to_date(day)
    return to_str(_day +datetime.timedelta(days=-num))

def to_str(day):
    return day.strftime('%Y-%m-%d')

def to_date(day):
    return datetime.datetime.strptime(day,'%Y-%m-%d')

def sub(day,num):
    return to_str(to_date(day) + datetime.timedelta(days=num))

def before(day1,day2):
    return to_date(day1) < to_date(day2)

def after(day1,day2):
    return to_date(day1) > to_date(day2)

def interval_days(day1,day2):
    return (to_date(day1)-to_date(day2)).days


if __name__ == '__main__':
    print get_day()
    print add("2017-01-30",5)
    print add("2017-01-03", 5)
    print before('2017-01-03','2017-01-04')
    print before('2017-01-05', '2017-01-04')
    print after('2017-01-05', '2017-01-04')
    print after('2017-01-05', '2017-01-08')
    print interval_days('2017-01-05', '2017-01-08')