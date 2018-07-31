#! /usr/bin/python
# coding:utf-8


class ExceptTest(Exception):

    @staticmethod
    def deal(name):
        r = input('hello, {value}'.format(value=name))
        try:
            print(r)
        except ValueError:
            raise

    @staticmethod
    def deal_1(name):
        try:
            print(name + "," + "hello")
        except TypeError:
            raise Exception("类型错误")

    @staticmethod
    def deal_2(name):
        try:
            print(name + "," + "hello")
        except TypeError:
            return Exception("类型错误")

    @staticmethod
    def deal_3(name):
        try:
            print(name + "," + "hello")
        except TypeError:
            print("传值类型错误")

    @staticmethod
    def deal_4(name):
        try:
            print(name + "," + "hello")
        except TypeError as info:
            print("传值类型错误: %s" % info)


if __name__ == '__main__':
    e = ExceptTest()
    e.deal_4(name=1)
    e.deal_1(name='Jay')
    e.deal_2(name=1)
    e.deal_3(name=1)
    e.deal(name="wudi")
    e.deal_1(name=1)
