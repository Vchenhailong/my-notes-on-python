#! /usr/bin/python
# coding:utf-8


def p(para1: str, para2: int) -> str:
    print("annotations:", p.__annotations__)
    return para1 + str(para2)


p('1', 1)
p('1', '1')
