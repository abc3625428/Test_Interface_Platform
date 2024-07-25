import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt
import pandas as pd


data = [[1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [3, 63, 93, 12, 15],
        [4, 83, 12, 16, 203],
        [53, 10, 15, 202, 25]]

# 将矩阵数据转换为 Pandas 数据框
df = pd.DataFrame(data, columns=["A", "B", "C", "D", "E"])
print(df)
# 创建折线图
plt.plot(df["A"], label="A")
plt.plot(df["B"], label="B")
plt.plot(df["C"], label="C")
plt.plot(df["D"], label="D")
plt.plot(df["E"], label="E")
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Line Map")
plt.legend()
plt.show()

# 创建柱状图
plt.bar(df.index,df["A"], label="A")
plt.bar(df.index,df["B"], label="B")
plt.bar(df.index,df["C"], label="C")
plt.bar(df.index,df["D"], label="D")
plt.bar(df.index,df["E"], label="E")
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("柱状图")
plt.legend()
plt.show()