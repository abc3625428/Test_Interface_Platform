# 读取excel表数据
import xlrd
import pandas as pd


from common.public import filePath_model,wt_filePath_model
import os


class OperationExcel:

    def __init__(self,num=0):
        self.num = num

    # 获取shell表
    def getSheet(self):
        book = xlrd.open_workbook(filePath_model())
        return book.sheet_by_index(self.num)

    # 以列表形式读取出所有数据
    def getExceldatas(self):
        data = []
        title = self.getSheet().row_values(0)
        for row in range(1, self.getSheet().nrows):
            row_value = self.getSheet().row_values(row)
            data.append(dict(zip(title,row_value)))
        return data

# 写入excel文件
def wirteExceldatas(data, file_path=wt_filePath_model()):

    df = pd.DataFrame(data)
    print(df)
    # if os.path.exists(file_path):
    #     existing_df = pd.read_excel(filePath_model())
    #     df = pd.concat([existing_df, df])
    df.to_excel(file_path, sheet_name='Sheet1', index=False, header=False)





#对excel表头进行全局变量定义
class ExcelVarles:

    sort = "序号"
    dataset="数据集"
    version= "版本"
    metric= "计数"
    mode= "模型"
    vllm = "得分"
