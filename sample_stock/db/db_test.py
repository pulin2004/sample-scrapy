# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: pulin

from db_pool import getPTConnection as db
import traceback

def TestMySQL():
    # SQL 查询语句;
    sql = "SELECT * FROM auth_user";
    try:
        # 获取所有记录列表
        db.cursor.execute(sql)
        results = db.cursor.fetchall();
        for row in results:
            userId = row[0]
            password = row[1]
            name = row[4]
            createTime = row[10]
            # 打印结果
            print ("userId=%d,password=%s,sex=%s,createTime=%s" %(userId, password, name, createTime ))
    except:
        print ("Error: unable to fecth data")
        traceback.print_exc()

TestMySQL()