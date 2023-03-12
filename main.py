import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC,SVC
from sklearn.ensemble import _gradient_boosting ,AdaBoostClassifier
# _gradient_boosting.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score


def transform(y_train):

    y_train_vals = []
    for i in y_train:
        if i == 'love':
            y_train_vals.append(0)
        elif i == 'anger':
            y_train_vals.append(1)
        elif i == 'surprise':
            y_train_vals.append(2)
        elif i == 'joy':
            y_train_vals.append(3)
        elif i == 'sadness':
            y_train_vals.append(4)
        elif i == 'fear':
            y_train_vals.append(5)
    return y_train_vals


def transform_decode(val):
    y_vals = []
    for i in val:
        if i == 0:
            y_vals.append("love🥰")
        elif i == 1:
            y_vals.append("anger😡")
        elif i == 2:
            y_vals.append('surprise 😮')
        elif i == 3:
            y_vals.append('joy 😃')
        elif i ==4:
            y_vals.append( 'sadness 😔')
        elif i == 5:
            y_vals.append("fear 😨")
    return y_vals

data_train = pd.read_csv("train.txt",sep=";")
# print(data_train)
data_train = data_train.rename(columns={'i didnt feel humiliated':'text','sadness':'emotions'})
# data_train.text = data_train['text']
data_train.text = data_train.text.apply(str.lower)
data_train.emotions = data_train.emotions.apply(str.lower)
x_train = data_train['text']
y_train = data_train['emotions']
print("data set done ........")
data_test = pd.read_csv("test.txt",sep=";")
data_test = data_test.rename(columns={'im feeling rather rotten so im not very ambitious right now':'text','sadness':'emotions'})
# print(data_test)
data_test.text = data_test.text.apply(str.lower)
data_test.emotions = data_test.emotions.apply(str.lower)

x_test = data_test['text']
y_test = data_test['emotions']

Vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, stop_words='english')
print("vectorization complete.......")
x_train = Vectorizer.fit_transform(x_train).toarray()
y_train = transform(y_train)
x_test = Vectorizer.transform(x_test).toarray()
y_test = transform(y_test)
# pickle.dump(Vectorizer,open("vectoriser.pkl","wb"))
# print(x_test)
# model = AdaBoostClassifier(LinearSVC(),algorithm='SAMME')
# model = LinearSVC()
model = SVC(kernel="rbf",random_state=0)
print("started training....")
model.fit(x_train,y_train)
print("Training complete......")
# print(x_test)
y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)
# accuracy = accuracy_score(y_train,y_pred)

print(f'{round(accuracy*100,2)}%')
a = input("enter the text : ")
a_p = Vectorizer.transform([a])
val = model.predict(a_p)
val = transform_decode(val)
print(*val)
# pickle.dump(model,open("text_emotion.pkl",'wb'))