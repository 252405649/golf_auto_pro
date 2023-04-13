
import os
import pytest
import allure
from common.handle_path import DATA_DIR, BASE_DIR
from common.handle_conf import conf
from common.handle_pandas_sheet import HandlePandasSheet
from common.template_util import get_extracts, refresh
from common.handle_log import my_log
from common.requests_util import RequestUtil
from common.params_util import is_json_str
import pandas as pd
data_list = HandlePandasSheet(DATA_DIR+'/golf_data.xlsx').read_data()
extract_obj = {}


@allure.epic("高尔夫项目")
@allure.suite('集成测试')
class TestLinks(object):

    @pytest.mark.parametrize("sheet_name, case_list", globals()['data_list'])
    def test_case_excel(self, sheet_name, case_list):
        # 读取业务场景
        allure.dynamic.title(sheet_name)
        # 读取场景下的用例
        for case in case_list:
            case_name, case_id, api_path, mthod,case_headers, case_params, case_assert, json_extract, remarks = case
            with allure.step('链路测试步骤'+case_id+":"+case_name):
                print('111111')
            # 读取上一个接口json提取的数据, 如果是token
            # 判断上一个接口是否有提取值，有则渲染到下一个接口的请求对象
            params={}
            headers={}
            if not pd.isna(case_params) and is_json_str(case_params):
                 params = eval(case_params)
            if not pd.isna(case_headers):
                headers = eval(case_headers)
            extract_obj = globals()['extract_obj']
            if extract_obj:
                # 当前接口定义格式化请求头和请求体
                refresh(params, extract_obj)
                refresh(headers, extract_obj)
            url = conf.get('env', 'base_url') + api_path
            my_log.info("-----------请求头：{}请求体：{}请求地址：{}请求类型:{}----------------headers---".format(headers, params, url, mthod))
            data = RequestUtil().send_request(
                method=mthod.upper(),
                url=url,
                headers=headers,
                data=params
            )

            my_log.info("用例返回：{}".format(data))
            # 提取json对象，下一个接口调用
            ext = get_extracts(json_extract, data)
            # 这个地方考虑链路测试：传递参数时只传递下一个接口，还是整个链路测试共享
            # 具体根据业务场景考虑，当前只传递下一个接口
            globals()['extract_obj'].update(ext)
            my_log.info("用例json提取：{}".format(ext))
            # globals()['extract_obj'] = ext
            if ext:
                my_log.info("用例--【{}】--传递了参数【{}】到下一个接口".format(case_name, ext))
            is_pass = case_assert == data['msg']
            if is_pass:
                my_log.info("用例--【{}】--执行通过".format(case_name))
            else:
                my_log.info("用例--【{}】--执行失败,原因:".format(case_name))
            assert is_pass


if __name__ == '__main__':
    # allure 必须在项目根目录执行，当前路径无效
    pytest.main(['-s', BASE_DIR+'/test_links.py', '--alluredir', BASE_DIR+'/report/result'])
    os.system(f"allure generate {BASE_DIR}/report/result -o {BASE_DIR}/report/html --clean")