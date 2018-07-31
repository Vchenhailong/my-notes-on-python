#! /usr/bin/python
# coding:utf-8

"""
contractor, property, iterator & generator:
    —— To create objects what can act as a sequence or mapping. For activating the objs,
    should implement the following contractors:

    __len__(self),
    __getitem__(self, key),
    __setitem__(self, key, value),
    __delitem__(self, key)

    Note: immutable objs need to implements 2 methods, mutable objs need 4 methods.

property: @see contractors.py
@property: to get the attributes

@staticmethod: 静态方法，其定义中没有参数 self，可直接通过类来调用。
@classmethod: 类方法，其定义中包含类似于 self 的参数，通常被命名为 cls.

iterator: Any objs implement __iter__ method, and it will contains __next__ method.

生成器：yield 语句

构造器、属性、迭代器和生成器：
    —— 可创建基于序列或映射的对象。为了使之有效，按需实现下列构造方法：

    __len__(self),
    __getitem__(self, key),
    __setitem__(self, key, value),
    __delitem__(self, key).

    注意：不可变对象需 要实现2个方法，而可变对象需要实现4个

property：见 contractors.py
@property：属性取值器

@staticmethod：静态方法，其定义中没有参数 self，可直接通过类来调用。
@classmethod: 类方法，其定义中包含类似于 self 的参数，通常被命名为 cls.

iterator: 任何实现了 __iter__ 方法的对象。

"""