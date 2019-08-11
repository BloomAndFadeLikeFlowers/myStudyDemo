print(__doc__)

# 本章主要讲述一些用于回归的方法，其中目标值 y 是输入变量 x 的线性组合。 数学概念表示为：如果 \hat{y} 是预测值，那么有：
# y^ (w, x) = w_0 + w_1 x_1 + ... + w_p x_p
#
# 在整个模块中，我们定义向量 w = (w_1,..., w_p) 作为 coef_ ，定义 w_0 作为 intercept_ 。
# LinearRegression 拟合一个带有系数 w = (w_1, ..., w_p) 的线性模型，使得数据集实际观测数据和预测数据（估计值）之间的残差平方和最小。其数学表达式为:
# min(w) || X_w - y || 2^ 2

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

print("diabetes： %s", str(diabetes))

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]
print("diabetes_X： %s", str(diabetes_X))

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
print("diabetes_X_test： %s", str(diabetes_X_test))

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
print("diabetes_y_test： %s", str(diabetes_y_test))

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)
print("diabetes_y_pred： %s", str(diabetes_y_pred))

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
