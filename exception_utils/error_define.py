#! /usr/bin/python
# coding:utf-8


class StaticErrMsg(Exception):

    login_error = ['U0001', '账户或密码错误']


if __name__ == '__main__':
    print(StaticErrMsg.login_error)
