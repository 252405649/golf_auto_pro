import json
from string import Template
import jsonpath


class MyTemplate(Template):
    delimiter = "!"


# data 要被格式化的数据： [{"token": "!token", "zz": "wwqwe"},{"token": "!token", "ff": "ssada"}]
# context  对于格式化的内容：{"token": "1234"}
def refresh(data, context):
    # 变量渲染
    print("渲染内容----------", data)
    if type(data) == dict:  # 字典类型
        for key in data.keys():
            value = data.get(key)
            if value is None:
                continue
            data.update({key: refresh(value, context)})
    elif type(data) == list:  # list类型
        tmp_list = []
        for item in data:
            tmp_list.append(refresh(item, context))
        return tmp_list
    elif type(data) == str:  # 字符串类型
        # print('字符串转换-------', data, context)
        value = MyTemplate(data).safe_substitute(**context)
        return value
    else:
        return data


# 提取返回接口的传递参数
def get_extracts(extract, reps):
    """
    :param extract 提取规则
    :parame reps  接口返回的对象
    :return 传递下一个接口的参数字典
    """
    extract_data = {}
    # 判断提取规则必须非空，且是字典类型
    if type(extract) == str and extract and type(json.loads(extract)) == dict:
        extract_data = json.loads(extract)
        for key in extract_data:
            extract_data[key]
            # 读取对于的规则下对于的参数值:
            # 返回的是数据，调试时候发现这里报错
            # 存在返回数组[], 不存在返回false,不判断取下标0时候报错
            if jsonpath.jsonpath(reps, extract_data[key]):
                extract_data[key] = jsonpath.jsonpath(reps, extract_data[key])[0]
    return extract_data

# #  把前一个接口提取的参数，传递到下一个接口
# def read_extracts(data, extract, reps):
#     # 判断提取规则必须非空，且是字典类型
#     if extract is not None and type(json.loads(extract)) == dict:
#         extract_data = json.loads(extract)
#         for item in extract_data.items():
#             # 读取对应提取的对象名称
#             key = item[0]
#             # 读取对应提取的路径(规则)
#             path = item[1]
#             # 读取对于的规则下对于的参数值:
#             # 返回的是数据，调试时候发现这里报错
#             # 存在返回数组[], 不存在返回false,不判断取下标0时候报错
#             if jsonpath.jsonpath(reps, path):
#                 value = jsonpath.jsonpath(reps, path)[0]
#                 context = {key: value}
#                 refresh(data, context)
#     return data


if __name__ == '__main__':
    # # 1.refresh接口测试
    # # a = {"token": "!token"}
    # # a = {"token": "!token", "zz": "wwqwe"}
    # a = [{"token": "!token", "zz": "wwqwe"},{"token": "!token", "ff": "ssada"}]
    # b= {"token": "1234"}
    # refresh(a, b)
    # print(a)

    # # 2.read_extracts 接口测试
    # data2 = {"content-type": "application/json", "authorization": "!token", "id": "!id"}
    # extracts = '{"token": "$.token", "id": "$.id"}'
    # rep = {"token": "sadhakj1232131op", "id": "1114"}
    # rep2 = {"token": "sadhakj1232131op"}
    # read_extracts(data2, extracts, rep)
    # print('a--data-----------', data2)

    #3.get_extracts接口测试
    data2 = {"content-type": "application/json", "authorization": "!token", "id": "!id"}
    extracts = '{"token": "$.token", "id": "$.id"}'
    extracts2 = '{"token": "$.token", "id": "$.id", "zz": "$.zz"}'
    # rep = {"token": "sadhakj1232131op", "id": "1114"}
    # a = get_extracts(extracts, rep)
    # print('--------a---', a)
    data3={"pageSize": "!token","pageNum":"sdasdasdda","id":"!id", "zz":2222}
    refresh(data3, {"token":"212313", "id":"9999"})
    print('data2--------', data3)

