#! /usr/bin/python
# coding:utf-8


import random


class Choice:

    def __init__(self):
        pass

    @staticmethod
    def make_choice():
        # 返回从0~1的随机实数
        c1 = random.random()
        print('返回从0~1的随机实数: %s' % c1)

        # 返回一个 a~b(含) 的随机实数
        c2 = random.uniform(1, 1000)
        print('返回一个 a~b(含) 的随机实数: %s' % c2)

        # 从range(start, stop, step) 中随机选择一个数
        c3 = random.randrange(1, 100, 2)
        print('从range(start, stop, step) 中随机选择一个数: %s' % c3)

        # 从序列 seq 中随机地选择一个元素
        seq = [2, 4, 6, 8]
        c4 = random.choice(seq)
        print('从序列 seq 中随机地选择一个元素: %s' % c4)

        # 从序列 seq 中随机地选择 n 个值不同的元素
        seq = [1, 3, 5, 7, 9]
        c5 = random.sample(seq, 3)
        print('从序列 seq 中随机地选择 n 个值不同的元素: %s' % c5)

        # 返回一个 a~b(含) 的整型随机数
        c6 = random.randint(0, 9)
        print('返回一个 a~b(含) 的整型随机数 : %s' % c6)


class GenMobile:

    def __init__(self):
        # 因为在 python 中，字符串也是序列
        self.__first = '1'
        self.__second = random.choice('34579')
        self.__third = '0123456789'

    def generator(self):
        suffix = ''
        for i in range(len(self.__third)-1):
            itr = random.choice(self.__third)
            suffix = suffix + itr
        print('生成的手机号为：%s' % (self.__first + self.__second + suffix))
        return self.__first + self.__second + suffix


if __name__ == '__main__':
    Choice.make_choice()
    c = Choice()
    g = GenMobile()
    result = g.generator()
    print(result)

