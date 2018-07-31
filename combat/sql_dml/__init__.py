#! /usr/bin/python
# coding:utf-8

"""
创建一个连接引擎
engine=create_engine("mysql+pymysql://root:a5230411@localhost:3306/test",echo=True)
我们将连接引擎放到engine里面方便后面使用。
create_engine("数据库类型+数据库驱动://数据库用户名:数据库密码@IP地址:端口/数据库"，其他参数)
上文当中echo=True是开启调试，这样当我们执行文件的时候会提示相应的文字

"""