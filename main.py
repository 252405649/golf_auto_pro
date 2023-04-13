import allure
import pytest
import os
import time
from common.handle_path import BASE_DIR
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_name = os.path.basename(__file__).split('.')[0]  # 获取档前的文件名称（不带后缀），作为存放
    time_stamp = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))   # 用时间戳生成一串不重复的数字
    html_path = f'{BASE_DIR}/report/html/'
    if not os.path.exists(html_path):
        os.makedirs(html_path)
    new_dir_name = str(file_name) + time_stamp  # 生成测试报告文件名称
    new_html_path = f'{BASE_DIR}/report/html/' + new_dir_name  # 生成html报告文件名称
    os.mkdir(new_html_path)
    # pytest.main(['-s', '-v', f'--env={ENV_Default}', f'{BASE_DIR}/conftest.py::test_start'])
    pytest.main(['-s', './testcases/test_link.py',
                 './testcases/test_link.py',
                 '--reruns=1', '--reruns-delay=2',
                 '--alluredir', f'{BASE_DIR}/report/result/' + new_dir_name])
    # 设置allure报告的环境变量
    os.system(f"copy {BASE_DIR}/environment.properties {BASE_DIR}/report/result")
    os.system(f"allure generate {BASE_DIR}/report/result/{new_dir_name} -o {BASE_DIR}/report/html/{new_dir_name} --clean")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
