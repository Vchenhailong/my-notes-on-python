#! /usr/bin/python
# coding:utf-8
import webbrowser
from fileinput import close


def file_reader():
    try:
        for line in open("/Users/hailongchen/Desktop/测试数据"):
            print(line, end=' ')
    # 捕获异常
    except (FileExistsError, BaseException):
        # 抛出异常
        raise Exception
    # 无论如何，最终将之关闭（这里不一定是个正确的示例，只为表示 finally 的作用）
    finally:
        close()


def file_reader_2():
    # The with statement allows objects like files to be used in
    # a way that ensures they are always cleaned up promptly and correctly.
    with open("hello.txt") as f:
        for line in f:
            print(line, end=' ')


def browser():
    webbrowser.open('http://www.baidu.com')


# file_reader()
# file_reader_2()
browser()

