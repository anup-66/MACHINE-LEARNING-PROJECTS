X =[[5],[10],[15],[20],[25]]
# y=["song","series","theater","bhajan","movie"]
# X = [["y","F","H","H"],["y","M","L","H"],["m","M","L","H"],["s","F","N","H"],["m","F","L","H"]]
y=["dy","dc","dc","dx","dy"]

from sklearn.neighbors import KNeighborsClassifier
nei = KNeighborsClassifier(n_neighbors=5)
nei.fit(X,y)

ace = nei.predict([[1]])
# ace = nei.predict([["m","M","L","H"]])

# ace=nei.predict([[1]])
# from sklearn.metrics import accuracy_score
# all = accuracy_score(ace,y)
print(ace)
# print(all)


