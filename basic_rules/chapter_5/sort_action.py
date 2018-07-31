#! /usr/bin/python
# coding:utf-8


def do_sort():
    # 冒泡排序要排序n个数，由于每遍历一趟只排好一个数字，
    # 则需要遍历n-1趟，所以最外层循环是要循环n-1次，而
    # 每趟遍历中需要比较每归位的数字，则要在n-1次比较
    # 中减去已排好的第i位数字，即每趟循环要遍历是n-1-i次
    lst = [1, 4, 3, 5, 2]
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]   # 这里使用的是序列解包进行值互换

    print(lst)


do_sort()
