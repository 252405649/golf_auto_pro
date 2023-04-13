import pandas as pd

class HandlePandasExcel:
    def __init__(self, filename, sheetname):
        # filename   excel文件名称（路径）
        # sheetname    表单名称
        self.filename = filename
        self.sheetname = sheetname

    def read_data(self):
        print('path-------', self.filename)
        data = pd.read_excel(self.filename, sheet_name=self.sheetname)
        rows = data.shape[0]
        columns = data.shape[1]
        list = []
        list2 = []
        # 读取数据
        for row in range(0, rows):
            for col in range(0, columns):
                list2.append(data.iloc[row, col])
                print(data.iloc[row, col])
            list.append(list2)
            list2 = []
        return list

    # 创建excel
    def create_excel(self):
        df = pd.DataFrame()
        df.to_excel(self.filename, sheet_name=self.sheetname, index=False)

    # 数据写入的方法
    def write_data(self, row, column, value):
        data = pd.read_excel(self.filename)
        data.iloc[row, column] = value


if __name__ == '__main__':
    excel = HandlePandasExcel(r'D:\自动化视频\接口自动化视频\用例数据要求基础模板.xlsx', 'register')
    res = excel.read_data()
    print(res)

