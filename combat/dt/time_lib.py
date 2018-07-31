#! /usr/bin/python
# coding:utf-8


import time
from datetime import time, timedelta, datetime, date


class Dat:

    # def __init__(self):
    #     self.year = '1970'
    #     self.month = '1'
    #     self.day = '1'
    #     self.hour = '00'
    #     self.minute = '00'
    #     self.second = '00'
    #     # 当前时间
    #     print(time.asctime())
    #     # 格式化当前时间
    #     print(time.strftime('%Y-%m-%d'))
    #
    # def get_datime(self):
    #     return self.year, self.month, self.day, self.hour, self.minute, self.second
    #
    # def set_datime(self, datm):
    #     self.year, self.month, self.day, self.hour, self.minute, self.second = datm
    #
    # dattime = property(get_datime, set_datime)

    def getDatetimeToday(self):
        t = date.today()  # date类型
        # print('today is' + ' ' + str(t))
        return t

    def getDatetimeYesterday(self):

        today = self.getDatetimeToday()  # datetime类型当前日期
        yesterday = today - timedelta(days=1)  # 减去一天
        print(type(yesterday))
        print('yesterday is' + ' ' + str(yesterday))
        return yesterday


if __name__ == '__main__':
    d = Dat()
    # time.strftime('%Y-%m-%d', d.dattime)
    #
    # print(d.dattime)
    d.getDatetimeYesterday()
    d.getDatetimeToday()
