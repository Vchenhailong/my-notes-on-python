#! /usr/bin/python
# coding:utf-8

from math import pi


class StringFormat:

    @staticmethod
    def string_format():
        string = 'Hey, %s. %s enough for ya?'
        values = ('guys', 'Hot')
        # This is simple-format
        # 简单字符串格式化方法
        print(string % values)
        # This is standard format
        # 标准字符串格式化方法
        string_d = 'Hello, {1}. {0} enough for ya?'.format("Hot", "guys")
        print(string_d)
        # This is for remaining 2 decimals
        # 保留2位数
        print("{name} is approximately {value:.2f}.".format(value=pi, name="π"))
        # transfer symbol
        # 转换标识符
        print("{pi!s} {pi!r} {pi!a}".format(pi="π"))

    @staticmethod
    def string_sub(string='Hello'):
        if string.find('o') != -1:
            print('find one character:o')
            print('the first index of substring is:' + str(string.find('o')) + " position")
        else:
            print("nothing")


if __name__ == '__main__':
    StringFormat.string_format()
    StringFormat.string_sub()
