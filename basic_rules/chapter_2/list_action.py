#! /usr/bin/python
# coding:utf-8


class ListAction:

    def __init__(self):
        pass

    @staticmethod
    def list_init():
        greeting = [None]
        print(greeting)

    @staticmethod
    def list_index():

        # note: Do not be out of range
        # 注意：别越界
        greeting = 'hello'
        print(greeting[0])

    @staticmethod
    def list_slicing():
        greeting = 'hello'
        print(greeting[2:3])

    @staticmethod
    def list_slicing_step():
        # note: the third num means the step.The num is 1 Default.
        # 注意：第三位数意味着步长，默认步长为1
        greeting = 'hello'
        print(greeting[::2])

    @staticmethod
    def list_connect():
        greeting = 'hello'
        friend = 'world'
        print(greeting + '' + friend)

    @staticmethod
    def list_duplicated():
        greeting = 'hello'
        print(greeting * 3)

    @staticmethod
    def list_in():
        greeting = input("Input one character:")
        if 'o' in str(greeting):
            print(True)
        elif 'O' not in str(greeting):
            print('O is not in the list')
        else:
            print('Input character O')

    @staticmethod
    def list_length():
        greeting = input("Input something,I can calculate the length:")
        print('OK, Length is' + ' ' + str(len(greeting)))

    @staticmethod
    def to_list(para):
        print(list(para))

    @staticmethod
    def list_to_string(lst):
        try:
            to_string = ''.join(lst)
            print(to_string)
        except TypeError:
            print('must be string-list')

    @staticmethod
    def act():
        lst = list()
        lst.append('li')
        lst.extend(['st'])
        print(lst)


if __name__ == '__main__':
    ListAction.list_init()
    ListAction.list_index()
    ListAction.list_slicing()
    ListAction.list_duplicated()
    ListAction.list_slicing_step()
    ListAction.list_in()
    ListAction.list_connect()
    ListAction.list_length()
    ListAction.to_list('HELLO')
    ListAction.list_to_string(lst=['1', '2'])
    ListAction.act()
