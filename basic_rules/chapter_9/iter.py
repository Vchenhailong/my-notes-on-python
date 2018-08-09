#! /usr/bin/python
# coding:utf-8
import sys


# 迭代器有两个基本方法。  iter()和next()
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
def iter_action():
    lst = ['a', 'b', 'c', 'd']
    it = iter(lst)
    # 获取下一个迭代数据
    print('next is' + next(it))
    # 以遍历方式1
    for i in it:
        print('.....' + ' ' + i)
    # 以遍历方式2
    while True:
        try:
            print('__next__() call' + ' ' + it.__next__())
        except StopIteration:
            sys.exit()


iter_action()
