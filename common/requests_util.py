import json
import re
import requests
from common.params_util import dict_to_str
from common.handle_log import my_log

class RequestUtil:
    # 类变量：通过类名访问
    session = requests.session()

    def send_request(self, method, headers, url, data, **kwargs):
        """
        :param method:  请求类型
        :param url:  请求地址
        :param data: 请求参数
        :param kwargs: 拓展字段
        :return:
        """

        method = str(method).upper()
        rep = None
        if method == 'GET':
            rep = RequestUtil.session.request(method, url=url, headers=headers, params=data, **kwargs)
            return rep.json()
        elif method == 'POST':
            # print('data-----------', json.dumps(headers))
            if re.search('application/x-www-form-urlencoded', json.dumps(headers)):
                data_str = dict_to_str(data)
                rep = RequestUtil.session.post(url=url, headers=headers, data=data_str, **kwargs)
            else:
                rep = RequestUtil.session.post(url=url, headers=headers, json=data, **kwargs)
            return rep.json()
        else:
            my_log.error('当前请求类型不支持--{}',method)


