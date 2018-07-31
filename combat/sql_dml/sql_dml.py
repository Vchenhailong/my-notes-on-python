#! /usr/bin/python
# coding:utf-8


from sqlalchemy import create_engine, String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
import json


# 本地数据库： $ mysql -u root -p

def conn_mysql():
    engine = create_engine("mysql+pymysql://root:hailongchen123@localhost:3306/ifsys", encoding="utf-8",
                           echo=True)
    engine.connect()


conn_mysql()
