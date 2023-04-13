def login_check(username=None, password=None):
    """
    :param username: 账号
    :param password: 密码
    :return: dict type
    """
    if username != None and password != None:
        if username == 'sunk' and password == '123456':
            return {'code': 200, 'msg': "登录成功"}
        else:
            return {'code': 8001, 'msg': "账号或者密码错误"}
    else:
        return {'code': 8002, 'msg': "账号或者密码不能为空"}

if __name__ == '__main__':
    res = login_check('sunk', '123456')
    assert res['code'] == 200
    print(res)