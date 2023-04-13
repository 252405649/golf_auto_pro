import pytest


@pytest.fixture(scope="function", autouse=False, params=['张三', '李四', '王五'], name='db')
def execute_db_connection(request):
    print('执行数据库连接')
    yield request.param
    print('关闭数据库连接')


@pytest.fixture()
def fixtrue01():
    print('执行fixtrue01---')
