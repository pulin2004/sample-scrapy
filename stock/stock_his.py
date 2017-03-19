#!/usr/bin/python
#-*- coding: utf-8 -*-

import csv
import os


class Stock_His():
    #整个目录应该是{$__base_path}/{code}/code_yyyy_mm_dd-yyyy_mm_dd.csv
    __base_path ="./stock_his_data"
    def __init__(self,stock_code):
        pass

    def get_code_directory(self,stock_code):
        return os.path.join(self.__base_path ,stock_code)

