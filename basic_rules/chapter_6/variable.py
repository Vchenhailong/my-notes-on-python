#! /usr/bin/python
# coding:utf-8
# https://docs.python.org/3.6/tutorial/classes.html
# https://www.cnblogs.com/lijunjiang2015/p/7802410.html
# https://blog.csdn.net/Leo_Coding/article/details/72935271


def change(p):
    p = 'Mrs. chen'
    print(p)


def hello(*para):
    # *para : It means any numbers of parameters.Additional, the type of the para is a tuple.
    # *para : 表示参数para是不定数量的可选输入的，另外，它的类型是一个元组类型。
    print(para)   # 注意，这里不是 print(*para)
    print(type(para))


def hello_2(**para):
    # **para : It means collect the keyword parameters, the type is a dict.
    # **para : 表示参数para是搜集关键字参数的，类型为字典。
    print(para)
    print(type(para))


def assignment():
    # 序列解包
    # 代码相当于： x = 3; y = 4; temp = x; x = y; y = temp
    x, y = 3, 4
    x, y = y, x   # 将值互换（重新绑定）
    print(x, y)


# 在函数内部给参数赋值，对外部没有影响
change(p='Mr.chan')
hello(1, 2, 3)
hello_2(x=1, y=2)
assignment()


class A:
    # 定义类属性（类变量）, 可通过类名访问，其被所有实例共享
    word = 'hello'
    # 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。
    # 若内部变量标示，如： 当使用“from M import”时，不会将以一个下划线开头的对象引入。
    _p1 = 'Mr'
    # 双下划线的表示的是私有类型的变量。只能允许这个类本身进行访问了，连子类也不可以用于命名一个类属性（类变量）。
    # 调用时名字被改变（在类FooBar内部，__boo变成_FooBar__boo,如self._FooBar__boo）
    __p2 = 'Miss'

    def p(self):
        # 定义实例属性
        print(self.word)
        print(self._p1)
        print(self.__p2)

    def i(self):
        print(self.word)
        print(A._p1)
        print(A.__p2)


class B(A, Exception):

    pass


if __name__ == '__main__':
    a = A()
    a._p1 = '1'
    a.__p2 = '2'
    a.p()
    a.word = 'hi'
    a.i()
    a.__p2 = "what"

    b = B()
    # print(b._p1)
    # print(b.__p2)
