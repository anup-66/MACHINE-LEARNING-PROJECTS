# ace = [['y','F','H','H'],['y','M','L','H'],['m','M','L','H'],['s','F','N','H'],['m','F','L','H']]
ace = [[1,0,0,1],[1,1,0,1],[2,1,0,1],[3,0,2,1],[2,0,0,1]]
res=['dy','dc','dc','dx','dy']
from sklearn import tree
cal = tree.DecisionTreeClassifier()
all = cal.fit(ace,res)
pre = cal.predict([[2,9,0,1]])
# pre = cal.predict([['m','F','L','H']])
print(pre)