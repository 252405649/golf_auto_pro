"""
==========================
Author:sunk123
Time:2022-07-18 18:51
Company:力石科技有限公司
==========================
"""
import os
#项目的根目录的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用例数据所在目录
DATA_DIR = os.path.join(BASE_DIR, 'datas')

# 配置文件所在目录
CONF_DIR = os.path.join(BASE_DIR, 'conf')

# 日志文件所在目录
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 测试报告所在目录
REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# 测试用例所在目录
CASS_DIR = os.path.join(BASE_DIR, "testcases")
# print(CASS_DIR)


# from testcases import test_register
# os.path.abspath:给一个相对路径，获取绝对路径
# p2= os.path.abspath('..')
# print(p2)   C:\Users\Administrator\PycharmProjects\pythonProject

# n = __name__
# fp = __file__
# print(test_register.p_name)
# print(n)
# print(fp, '----')
# """
# 魔法变量：变量的值在不同的情况下是不一样的
# __name__:
#     启动文件中的__name__的值为：__main__
#     不是启动文件的情况下：打印的值为模块名
# __file__:代表当前文件的文件名字（pycharm 中运行时候会显示文件的绝对路径）
# """
# #获取当前文件的绝对路径
# p = os.path.abspath(__file__)
# print(p)