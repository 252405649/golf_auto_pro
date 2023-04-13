import os
import requests
import pytest
import json
import allure
from common.handle_path import DATA_DIR
from common.handle_pandas_excel import HandlePandasExcel
handleExcel = HandlePandasExcel(DATA_DIR+'/golf_data.xlsx', 'Sheet1')


class TestLogin:
    @pytest.mark.parametrize("case_name, case_id, case_url, mthod, headers, params, case_assert, json_extract", handleExcel.read_data())
    def test_case_excel(self, case_name, case_id, case_url, mthod, headers, params, case_assert, json_extract):
        allure.dynamic.title(case_id)
        allure.dynamic.description(case_name)
        print('casename--------',case_name)
        response = requests.request(
            url=case_url,
            headers=json.loads(headers),
            method=mthod.upper(),
            params=eval(params)
        )
        data = response.json()
        print('case_info---', data)
        assert case_assert == data['msg']


if __name__ == '__main__':
    pytest.main(["--alluredir", "./report/result", "test_login.py"])
    os.system("allure generate ./report/result -o ./report/html --clean")