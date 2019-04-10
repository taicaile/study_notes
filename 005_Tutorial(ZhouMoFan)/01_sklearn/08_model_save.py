from sklearn.externals import joblib
import pickle
from sklearn import svm
from sklearn import datasets

clf = svm.SVC()
iris = datasets.load_iris()
X, Y = iris.data, iris.target
clf.fit(X, Y)

# method 1: pickle

'''
with open('save/clf.picle', 'wb') as f:
    pickle.dump(clf, f)
'''

with open('save/clf.picle', 'rb') as f:
    clf2 = pickle.load(f)
    print(clf2.predict(X[0:1]))

# method 2: joblib
# save
joblib.dump(clf, 'save/clf.pkl')
# restore
clf3 = joblib.load('save/clf.pkl')
print(clf3.predict(X[0:1]))
