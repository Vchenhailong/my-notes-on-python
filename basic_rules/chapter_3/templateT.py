#! /usr/bin/python
# coding:utf-8


from string import Template


def tmplt_action():
    s1 = Template('$who likes $what')
    print(s1.substitute(who='tim', what='lisa'))


tmplt_action()
