from sklearn.datasets import make_regression,make_classification
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,r2_score
x,y = make_regression(n_samples=1000,n_features=4,n_informative=2,random_state=0,shuffle=False)
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0,test_size=.15)
regr = RandomForestRegressor(max_depth=2,random_state=0)
regr.fit(x_train,y_train)
pred_regr = regr.predict(x_test)
# print(pred_clif)
acc = accuracy_score(y_test,pred_regr)
# print(acc)
print(y_test)
print(pred_regr)
# val = r2_score(y_test,pred_regr)
# print(val)
# print(len(y_test))
# print(len(pred_regr))