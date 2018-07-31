#! /usr/bin/python
# coding:utf-8


class FlowControl:

    @staticmethod
    def foreach_1():
        word = 'string'
        for i in word:
            print(i)

    @staticmethod
    def foreach_2():
        for i in range(10):
            print(i)

    @staticmethod
    def foreach_3():
        word = 'string'
        for i in range(len(word)):
            print(word[i])

    @staticmethod
    def foreach_4():
        mapping = {'k1': 'v1', 'k2': 'v2'}
        for k, v in mapping.items():
            print(k, v)

    @staticmethod
    def judgement():
        try:
            age = int(input("what's your age: "))
            if 100 > age >= 18:
                print('已成年')
            elif 0 < age < 18:
                print('未成年')
            else:
                raise ValueError('输入不合法')
        except TypeError:
            raise ValueError('输入数字')

    @staticmethod
    def while_case():
        lst = [None]
        print('The initial length is: ' + str(len(lst)))
        while 1 <= len(lst) < 10:
            lst.append(len(lst) + 1)
            print('Now the length is: ' + str(len(lst)))

    @staticmethod
    def while_case_2(statement):
        while statement is not None:
            print('content is %s' % statement)
            return statement


if __name__ == '__main__':
    flow = FlowControl()
    flow.foreach_1()
    flow.foreach_2()
    flow.foreach_3()
    flow.foreach_4()
    flow.judgement()
    flow.while_case()
    flow.while_case_2("hello, world")
