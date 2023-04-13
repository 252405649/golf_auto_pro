import pandas as pd
from common.handle_path import DATA_DIR
from common.handle_log import my_log


class HandlePandasSheet:
    def __init__(self, filename):
        # filename   excel文件名称（路径）
        self.filename = filename

    def read_data(self):
        my_log.info("开始读取excel--【{}】--读取".format(self.filename))
        sheet = pd.read_excel(self.filename, sheet_name=None)
        sheet_list =[]
        # 循环所有的sheet
        for key, data in sheet.items():
            sheet_obj = ()
            my_log.info("开始读取sheet--【{}】--读取".format(key))
            rows = data.shape[0]
            columns = data.shape[1]
            print('----row-col-----', rows,columns)
            list = []
            list2 = []
            # 读取数据
            for row in range(0, rows):
                for col in range(0, columns):
                    list2.append(data.iloc[row, col])
                list.append(list2)
                list2 = []
            sheet_obj = (key, list)
            sheet_list.append(sheet_obj)
            sheet_obj=()
        return sheet_list

    # 创建excel
    def create_excel(self):
        df = pd.DataFrame()
        df.to_excel(self.filename, sheet_name=self.sheetname, index=False)

    # 数据写入的方法
    def write_data(self, row, column, value):
        data = pd.read_excel(self.filename)
        data.iloc[row, column] = value


if __name__ == '__main__':
    excel = HandlePandasSheet(DATA_DIR+'/golf_data.xlsx')
    res = excel.read_data()
    print(res)

