#! /usr/bin/python
# coding:utf-8


"""
正则
=================================
1.为表示模块re要求的单个反斜杠，需要在字符串中书写两个反斜杠，让解释器对其 进行转义
2.字符集只能匹配一个字符。开头添加脱字符(^)，可指定排除字符。如'[^abc]'，即与除 a、b和 c 外的其他任何字符都匹配。
3.二选一和子模式：管道符(|)。子模式即将"内容"和"管道"放在一组圆括号内
4.可选模式和重复模式：在"子模式"后面加上问号，将其指定为可选的，即可包含或可不包含
5.开头(^)和末尾($)
6.贪婪模式：尽可能多的进行匹配
7.非贪婪模式：符号(+?)
8.模板：字符串格式设置 —— '[something]'(字段)都替换为将something，作为Python表达式计算得到的结果
=================================
常用的方法
compile(pattern[, flags])               根据包含正则表达式的字符串创建模式对象
search(pattern, string[, flags])        在字符串中查找模式
match(pattern, string[, flags])         在字符串开头匹配模式
split(pattern, string[, maxsplit=0])    根据模式来分割字符串
findall(pattern, string)                返回一个列表，其中包含字符串中所有与模式匹配的子串
sub(pat, repl, string[, count=0])       将字符串中与模式pat匹配的子串都替换为repl
escape(string)                          对字符串中所有的正则表达式特殊字符都进行转义
"""