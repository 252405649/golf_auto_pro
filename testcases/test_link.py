import os
import requests
import pytest
import allure
from common.handle_path import DATA_DIR, BASE_DIR
from common.handle_conf import conf
from common.handle_pandas_excel import HandlePandasExcel
from common.template_util import get_extracts, refresh
from common.handle_log import my_log
handleExcel = HandlePandasExcel(DATA_DIR+'/golf_data.xlsx', '后台职称链路测试')
extract_obj = {}


@allure.epic('高尔夫自动化测试')
@allure.suite('单个链路测试')
class TestLink(object):

    @allure.story("查询后台订单")
    @pytest.mark.parametrize("case_name, case_id, api_path, mthod, case_headers, case_params, case_assert, json_extract, remark", handleExcel.read_data())
    def test_case_excel(self, case_name, case_id, api_path, mthod,case_headers, case_params, case_assert, json_extract, remark):
        allure.dynamic.title(case_name)
        allure.dynamic.description(case_id+":"+case_name)
        allure.dynamic.severity(allure.severity_level.NORMAL)  # 用例等级
        # 读取上一个接口json提取的数据, 如果是token
        # 判断上一个接口是否有提取值，有则渲染到下一个接口的请求对象
        params = eval(case_params)
        headers = eval(case_headers)
        extract_obj = globals()['extract_obj']
        if extract_obj:
            # 当前接口定义格式化请求头和请求体
            refresh(params, extract_obj)
            refresh(headers, extract_obj)
        url = conf.get('env', 'base_url')
        response = requests.request(
            url=url+api_path,
            headers=headers,
            method=mthod.upper(),
            params=params
        )
        data = response.json()
        my_log.info("用例返回：{}".format(data))
        # 提取json对象，下一个接口调用
        ext = get_extracts(json_extract, data)
        # 这个地方考虑链路测试：传递参数时只传递下一个接口，还是整个链路测试共享
        # 具体根据业务场景考虑，当前只传递下一个接口
        # globals()['extract_obj'].update(ext)
        globals()['extract_obj'] = ext
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
    pytest.main(['-s', BASE_DIR+'/test_link.py', '--alluredir', BASE_DIR+'/report/result'])
    os.system(f"allure generate {BASE_DIR}/report/result -o {BASE_DIR}/report/html --clean")