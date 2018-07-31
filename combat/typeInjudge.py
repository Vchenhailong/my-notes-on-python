#! /usr/bin/python
# coding:utf-8


# 类型判断
def is_blank(num):
    if isinstance(num, int) and num is not None:
        if num == 0:
            raise EOFError("内容为空")
        else:
            print(num)
            return True
    else:
        raise ValueError("非数字类型")


