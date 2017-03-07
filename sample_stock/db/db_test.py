# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: pulin


from db_pool import Mysql
# from _sqlite3 import Row

# 申请资源
mysql = Mysql()

sqlAll = "SELECT * FROM settings_item"
result = mysql.getAll(sqlAll)
if result:
    print "get all"
    for row in result:
        print "%s\t%s" % (row["id"], row["remark"])
result = mysql.getMany(sqlAll, 1)
if result:
    print "get many"
    for row in result:
        print "%s\t%s" % (row["id"], row["remark"])

result = mysql.getOne(sqlAll)
print "get one"
print "%s\t%s" % (result["id"], result["remark"])

# 释放资源
mysql.dispose()
