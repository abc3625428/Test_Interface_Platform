import xlrd
from common.public import filePath
class OperationExcel:
    # 获取shell表
    def getSheet(self, page):
        book = xlrd.open_workbook(filePath()) #前面已经默认将文件参数传递进去了,所以直接调用不片用再传参
        return book.sheet_by_index(page) #根据索引获取到Sheet表

    # 以列表形式读取出所有数据
    def getExceldatas(self, page=0):
        data = []
        title = self.getSheet(page).row_values(0)  # (0)获取第一行也就是表头
        for row in range(1, self.getSheet(page).nrows):  # 从第二行开始获取
            row_value = self.getSheet(page).row_values(row)
            data.append(dict(zip(title,row_value)))  # 将读取出每一条用例作为一个字典存放进列表
        return data


class ExcelVarles:
     start_work_year = '开始工作年份'
     born_year = '出生年份'