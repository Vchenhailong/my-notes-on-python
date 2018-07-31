#! /usr/bin/python
# coding:utf-8
import os
import xml.etree.ElementTree as ET
import configparser
import json


def config_file_reader():
    crt_path = os.path.abspath('.')
    up_path = os.path.abspath('..')

    conf_path = crt_path + "/config.ini"
    #
    parser = configparser.ConfigParser()
    parser.read(conf_path, encoding='utf-8')

    sects = parser.sections()
    o = parser.options('host')
    print(o)
    i = parser.items('host')
    print(i)

    r = parser.get('host', 'ip')
    print(r)






config_file_reader()
