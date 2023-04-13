"""
==========================
Author:sunk123
Time:2022-07-29 10:39
Company:力石科技有限公司
==========================
"""
import re

def replace_data(data, cls):
    """
    替换数据
    :param data: 要进行替换的用例数据（字符串）
    :param cls:  测试类
    :return: 返回结果
    """
    while re.search('#(.+?)#', data):
        res2 = re.search('#(.+?)#', data)
        item = res2.group()
        attr = res2.group(1)
        print('---------re go----------------', attr)
        value = getattr(cls, attr)
        data = data.replace(item, str(value))
    return data

def replace_data_con(data, config):
    """
    替换数据
    :param data: 要进行替换的用例数据（字符串）
    :param cls:  测试类
    :return: 返回结果
    """
    while re.search('#(.+?)#', data):
        res2 = re.search('#(.+?)#', data)
        item = res2.group()
        attr = res2.group(1)
        print('---------re go----------------', item)
        value = getattr(config, attr)
        data = data.replace(item, str(value))
    return data
class A:
    bb =1

if __name__ == '__main__':
    a = A()
    z=r'{"zz": "#bb#", "ff":"22"}'
    b = replace_data_con(z,a )
    print(b)