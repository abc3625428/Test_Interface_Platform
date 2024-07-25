import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# 数据集
# data = pd.read_csv('gold_prices.csv')  # 假设CSV文件包含日期和黄金价格



da = {'date':['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04','2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08','2020-01-09', '2020-01-10'],
      'Gold':[1.76405235,2.16420955,3.14294754,5.38384074, 7.25139873, 6.274120857, 22420927, 7.07285206, 6.96963321, 7.38023171]}

data = pd.DataFrame(da)
# np.random.seed(0)
# dates = pd.date_range('20200101', periods=10)
# print(dates,np.random.randn(10).cumsum())
# data = pd.DataFrame(np.random.randn(10).cumsum(), index=dates, columns=['date','Gold'])
print(data)

# 特征工程
def create_features(df, window_size=1):
    X, y = [], []
    for i in range(window_size, len(df)):
        X.append(df['Gold'].iloc[i - window_size:i].tolist())
        y.append(df['Gold'].iloc[i])
    return np.array(X), np.array(y)


X, y = create_features(data)

# X = np.reshape(X, (X.shape[0], X.shape[1], 1))
#

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # 训练模型
# model = LinearRegression()
# model.fit(X_train, y_train)

y = y.reshape(-1, 1)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测未来半年（按照月计算）
future_points = 6  # 6个月
last_known_price = data['Gold'].iloc[-1]
predicted_prices = []

for _ in range(future_points):
    # 假设我们基于当前最后已知价格进行简单预测（实际中应基于更复杂的时间序列预测）

    next_month_pred = model.predict(np.array([X_train[-1]]))[0]  # 简化的预测，仅作示例
    predicted_prices.append(next_month_pred)


# 输出预测结果
print("Predicted prices for the next 6 months:", predicted_prices)