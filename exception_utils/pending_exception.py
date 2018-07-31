#! /usr/bin/python
# coding:utf-8


class PException:

    def __init__(self, errcode, desc):
        self.errcode = errcode
        self.desc = desc
        raise Exception(errcode, desc)


if __name__ == '__main__':
    e = PException('U00002', '账号或密码错误')
