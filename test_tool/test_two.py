# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
#
# # 加载数据集
# cancer = load_breast_cancer()
#
# # 划分数据集为训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.2, random_state=42)
#
# # 创建并训练逻辑回归模型
# model = LogisticRegression(max_iter=1000)
# model.fit(X_train, y_train)
#
# # 使用模型进行预测
# y_pred = model.predict(X_test)
#
# # 计算预测准确率
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)
#


from sklearn.metrics import mean_squared_error
import numpy as np
import random

c = np.random.randint(1,35,5)
d = np.random.randint(1,13,2)
print(c,d,type(c))
# print(c+d)

print(mean_squared_error([27,22,3,3,28,9,11],[22,12,5,13,8,3,7]))
def predict_numbers():
    # 生成 7 个数字，前 5 个数字为 1-35，后两个数字为 1-12
    np.random.seed(0)
    numbers = np.random.randint(1, 36, 5)
    print(numbers)
    # 预测下一次的数字
    next_numbers = np.random.randint(1, 36, 5)

    # 计算预测值和实际值之间的均方误差
    mse = mean_squared_error(numbers, next_numbers)

    print(f"实际值: {numbers}")
    print(f"预测值: {next_numbers}")
    print(f"均方误差: {mse}")


predict_numbers()