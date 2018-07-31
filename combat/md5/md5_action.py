#! /usr/bin/python
# coding:utf-8


import hashlib


def file_md5():
    file_path = input("输入文件的绝对路径:")
    file = open(file_path)
    m_file_name = hashlib.md5(file.name.encode('utf-8'))
    m_file_content = hashlib.md5(file.read().encode('utf-8'))
    file.close()
    fr = m_file_name.hexdigest()
    cr = m_file_content.hexdigest()
    dic = {}
    dic.setdefault('文件名称-MD5', fr)
    dic.setdefault('文件内容-MD5', cr)
    print("=============" + "LOG START" + "==============")
    print(str(dic))
    print("=============" + "LOG   END" + "==============")


file_md5()
