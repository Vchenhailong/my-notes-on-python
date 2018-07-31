#! /usr/bin/python
# coding:utf-8

# 导入抽象类和抽象方法
from abc import ABC, abstractmethod


class A:

    def __init__(self):
        print('i am class A')

    @staticmethod
    def say():
        print('invoke function of the A')


class B:
    def __init__(self):
        print('i am class B')


class C:
    def __init__(self):
        print('i am class C')


class D(A, B, C):
    # 多重继承——不推荐使用
        super(A)
        print('i inherit A,B,C')

    # @staticmethod
    # def say():
    #     print('function of D')


class E(ABC):
    # 抽象方法（正确的使用待查阅更详细的资料）
    @abstractmethod
    def abstract_func(self):
        print('abstract')


class F(E):
    # 实现抽象类 E 的抽象方法
    def abstract_func(self):
        print('implements abstract func')


if __name__ == '__main__':
    a = A()
    d = D()
    d.say()
    f = F()
    isinstance(f, E)   # 先类型检查（True/False）
    f.abstract_func()  # 再去调用实现的抽象方法以确保无歧义
