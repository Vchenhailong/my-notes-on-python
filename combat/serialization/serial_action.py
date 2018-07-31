#! /usr/bin/python
# coding:utf-8
import json
import pickle


def serial_act():
    # JSON 模块，进行序列化和反序列化
    dic = {'age': 23, 'job': 'student'}
    dic_str = json.dumps(dic)     # 将对象转换成字符串
    print(type(dic_str), dic_str)

    dic_obj = json.loads(dic_str)     # 将字符串转换成字典对象
    print(type(dic_obj), dic_obj)




    # PICKLE 模块，以字节进行序列化和反序列化
    # 要存储在文件中，则使用方法 dump() 和 load()
    # 由于pickle写入的是二进制数据，所以打开方式需要以wb和rb的模式
    byte_data = pickle.dumps(dic)    # 返回存入的字节
    pickle.loads(byte_data)    # 将字节转换成对象
    # 序列化
    with open('abc.pkl', 'wb') as f:
        dic = {'age': 23, 'job': 'student'}
        pickle.dump(dic, f)
    # 反序列化
    with open('abc.pkl', 'rb') as f:
        aa = pickle.load(f)
        print(aa)
        print(type(aa))  # <class 'dict'>


serial_act()
