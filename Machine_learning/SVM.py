import sklearn.metrics

x = [[-1,1],[-2,-1],[1,1],[2,1]]
Y= [1,1,2,2]
# x = ["hihop","clasical","smoth","soft"]
# Y =[[0,1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
from sklearn.svm import SVC
clf = SVC()
clf.fit(x,Y)
print(clf.predict([[.8,-1]]))
arrr = clf.predict([[1,1],[2,-1],[-1,1],[2,-1]])
# arrr = clf.predict([[3],[6],[8.56]])
print(sklearn.metrics.accuracy_score(Y,arrr))
print(len(Y),len(arrr))