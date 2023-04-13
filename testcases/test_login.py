import os
import requests
import pytest
import json
import allure
from common.handle_path import DATA_DIR
from common.handle_conf import conf
from common.handle_pandas_excel import HandlePandasExcel
from common.var_util import get_extracts, refresh
handleExcel = HandlePandasExcel(DATA_DIR+'/golf_data.xlsx', 'Sheet1')


@allure.feature('业务流程测试')
class TestLogin():
    def setup_class(self):  # 仅类开始之前执行一次
        print("---setup_class---")
        self.extract_obj = {}

    @pytest.mark.parametrize("case_name, case_id, api_path, mthod, case_headers, case_params, case_assert, json_extract", handleExcel.read_data())
    def test_case_excel(self, case_name, case_id, api_path, mthod,case_headers, case_params, case_assert, json_extract):
        allure.dynamic.title(case_id)
        allure.dynamic.description(case_name)
        # 读取上一个接口json提取的数据, 如果是token
        # 判断上一个接口是否有提取值，有则渲染到下一个接口的请求对象
        params = eval(case_params)
        headers = eval(case_headers)
        extract_obj = json.loads(conf.get('env', 'extract_obj'))
        print('zzzz---------初始------',extract_obj)
        if extract_obj:
            print('extract_obj---',extract_obj)
            # 当前接口定义格式化请求头和请求体
            refresh(params, extract_obj)
            refresh(headers, extract_obj)
        print('casename--------',case_name)
        url = conf.get('env', 'base_url')
        response = requests.request(
            url=url+api_path,
            headers=headers,
            method=mthod.upper(),
            params=params
        )
        data = response.json()
        # 提取json对象，下一个接口调用
        ext = get_extracts(json_extract, data)
        print('-------------------ext----',ext)
        conf.set_config('env', 'extract_obj', json.dumps(ext))
        assert case_assert == data['msg']


if __name__ == '__main__':
    # allure 必须在项目根目录执行，当前路径无效
    pytest.main(['-s', 'test_login.py', '--alluredir', './report/result'])
    os.system("allure generate ./report/result -o ./report/html --clean")