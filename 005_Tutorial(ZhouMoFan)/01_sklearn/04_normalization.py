from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
from sklearn import preprocessing
import matplotlib.pyplot as plt

# data for normalization, each column can be consider a data range
a = np.array(
    [[10, 2.7, 3.6],
     [-100, 5, -2],
     [120, 20, 40],
     ], dtype=np.float64)
print("original data set : \n", a)
print("after normalization: \n", preprocessing.scale(a))


# data sets generating
X, Y = make_classification(n_samples=300, n_features=2, n_redundant=0,
                           n_informative=2, random_state=22, n_clusters_per_class=1, scale=100)

# X = preprocessing.minmax_scale(X, feature_range=(-1, 1))
# test without normalization
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
clf = SVC()
clf.fit(X_train, y_train)
print("without normalization performance:", clf.score(X_test, y_test))

# test with normalization
X = preprocessing.scale(X)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
clf = SVC()
clf.fit(X_train, y_train)
print("with normalization performance: ", clf.score(X_test, y_test))

# note: with scale, get 0.94; without scale, get 0.52
