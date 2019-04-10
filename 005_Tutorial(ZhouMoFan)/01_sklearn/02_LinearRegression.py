from sklearn import datasets
from sklearn.linear_model import LinearRegression

# load official data set
loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

# create a linear model class
model = LinearRegression()
# train the model
model.fit(data_X, data_y)

# print the predicted value
print(model.predict(data_X[:4, :]))
# print the label value
print(data_y[:4])
print("model intercept:", model.intercept_)
print("model coefficient:", model.coef_)
# R^2 coefficient of determination
print("model score:", model.score(data_X, data_y))
