import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# load the official data set
iris = load_iris()
X = iris.data
Y = iris.target


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=4)

# train model under the whole data set
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
print(knn.score(X_test, Y_test))


# trrain model under different trunks of the model, 5 round cross validation
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, Y, cv=5, scoring='accuracy')
print(scores.mean())

# to see the performance under different k values
k_range = range(1, 31)
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, Y, cv=10, scoring='accuracy')
    k_scores.append(scores.mean())

plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()
