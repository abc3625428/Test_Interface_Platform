import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt
import pandas as pd


class Data_Statistics:

    def __init__(self, data, columns, xlabel='Index', ylabel='Value', title='Data Map'):
        self.data= pd.DataFrame(data, columns)
        self.columns= columns
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title

    # 创建折线图
    def bar_chart(self):
        for i in range(len(self.columns)-1):
            plt.plot(self.data[self.columns[i]], label=self.columns[i])
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
        # plt.show()
        return plt

    # 创建柱状图
    def barchart(self):
        for i in range(len(self.columns) - 1):
            plt.plot(self.data[self.columns[i]], label= self.columns[i])
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
        # plt.show()
        return plt

    # 创建饼图
    def piechart(self):
        total_sum = self.data.sum()
        category_percentages = self.data.sum(axis=1) / total_sum * 100
        self.data.pie(category_percentages, labels=self.data.columns, autopct="%1.1f%%")
        return plt
