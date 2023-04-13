#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：golfProject002
@File ：params_util.py
@Author ：孙凯
@Date ：2023-03-31 2:40
@Description : 
'''
import json
from urllib import parse


def is_json_str(data):
    try:
        data_json = json.loads(data)
        return data_json
    except ValueError:
        return False

def dict_to_str(data):
    """
    从{"a":1,"b":2}转 a=1&b=2
    :param data:
    :return:
    """
    return parse.urlencode(data)


def str_to_dict(str_params):
    """
    从 a=1&b=2转{"a":1,"b":2}
    :param str_params:
    :return:
    """
    param_dict = {}
    list = str(str_params).split("&")
    for i in list:
        data = i.split("=")
        param_dict[data[0]] = data[1]
    return param_dict

if __name__ == '__main__':
    # bo = is_json_str('{"a":1}')
    bo = is_json_str('aa')
    print(bo)