import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([1,2,3,4,5,6]).reshape(-1,1)
y = np.array([6,1,9,5,17,12])
print("x.shape: ", x.shape)
print("y.shape: ", y.shape)

model=LinearRegression()
model.fit(x,y)
print("intercept: ", model.intercept_)
print("slope: ", model.coef_)

y_pred = model.predict(x)
print("predicted response: ", y_pred, sep='\n')

plt.scatter(x,y, color='blue')
plt.plot(x,y_pred, color='red' ,linewidth = 3)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
