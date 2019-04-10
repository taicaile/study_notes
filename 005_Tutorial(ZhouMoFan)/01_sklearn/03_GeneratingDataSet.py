import matplotlib.pyplot as plt
from sklearn import datasets

# generating data set
X, Y = datasets.make_regression(
    n_samples=100, n_features=1, n_targets=1, noise=10)
plt.scatter(X, Y)
plt.show()
