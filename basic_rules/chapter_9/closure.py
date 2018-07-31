#! /usr/bin/python
# coding:utf-8


def call(func):
    def wrapper():
        func()
        print(func.__name__)
    return wrapper
