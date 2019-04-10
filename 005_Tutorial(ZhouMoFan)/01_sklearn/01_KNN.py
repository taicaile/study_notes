import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# load official data set
iris = datasets.load_iris()

# get the features and label
iris_X = iris.data
iris_y = iris.target

# 70% data are used to train, and others for test
X_train, X_test, y_train, y_test = train_test_split(
    iris_X, iris_y, test_size=0.3)

# create a model class, with default parameters, and neighbors = 5
knn = KNeighborsClassifier()
# train the model with the train data
knn.fit(X_train, y_train)
# test model performance
y_test_result = [knn.predict(X_test) == y_test]

print("true error is :", np.count_nonzero(
    y_test_result.count)/np.shape(y_test_result)[1])
