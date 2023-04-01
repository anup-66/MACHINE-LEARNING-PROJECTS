# import pandas as pd
# from sklearn.model_selection import train_test_split
# data = pd.read_csv("Crop_recommendation.csv")
# label = data["label"]
# data = data.drop("label",axis=1)
# X_train,x_test,y_train,y_test = train_test_split(data,label,random_state=0,test_size=.20)
# # print(len(X_train))
# # print(len(x_test))
# # print(len(y_train))
# # print(len(y_test))
# from sklearn.svm import SVC
# from sklearn.ensemble import AdaBoostClassifier
# model =SVC(kernel='rbf')
# model.fit(X_train,y_train)
# y_pred = model.predict(x_test)
# from sklearn.metrics import accuracy_score
#
# accuracy = accuracy_score(y_test,y_pred)
# print(accuracy)
import numpy as np
array = np.array([62,52,16,22.27526694,58.84015925,6.9670577620000005,63.87020584])
array = array.reshape(1,-1)
print(array)
import pickle as pk
# file = open("trained_model.pkl","ab")
# pk.dump(model,file)
# file.close()
model = pk.load(open("trained_model.pkl","rb"))
give = model.predict(array)
print(give)