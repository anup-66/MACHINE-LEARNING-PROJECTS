import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

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
        elif i == 4:
            y_vals.append('sadness 😔')
        elif i == 5:
            y_vals.append("fear 😨")
    return y_vals
#
# data_train = pd.read_csv("train.txt", sep=";")
# data_train = data_train.rename(columns={'i didnt feel humiliated': 'text', 'sadness': 'emotions'})
# data_train.text = data_train.text.apply(str.lower)
# data_train.emotions = data_train.emotions.apply(str.lower)
#
# x_train = data_train['text']
# y_train = data_train['emotions']
#
# data_test = pd.read_csv("test.txt", sep=";")
# data_test = data_test.rename(columns={'im feeling rather rotten so im not very ambitious right now': 'text', 'sadness': 'emotions'})
# data_test.text = data_test.text.apply(str.lower)
# data_test.emotions = data_test.emotions.apply(str.lower)
#
# x_test = data_test['text']
# y_test = data_test['emotions']
#
# Vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, stop_words='english')
# x_train = Vectorizer.fit_transform(x_train)
# y_train = transform(y_train)
# x_test = Vectorizer.transform(x_test)
# y_test = transform(y_test)

data_train = pd.read_csv("train.txt",sep=";")
# print(data_train)
data_train = data_train.rename(columns={'i didnt feel humiliated':'text','sadness':'emotions'})
# data_train.text = data_train['text']
data_train.text = data_train.text.apply(str.lower)
data_train.emotions = data_train.emotions.apply(str.lower)
x_train = data_train['text']
y_train = data_train['emotions']

data_test = pd.read_csv("test.txt",sep=";")
data_test = data_test.rename(columns={'im feeling rather rotten so im not very ambitious right now':'text','sadness':'emotions'})
# print(data_test)
data_test.text = data_test.text.apply(str.lower)
data_test.emotions = data_test.emotions.apply(str.lower)

x_test = data_test['text']
y_test = data_test['emotions']


Vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, stop_words='english')

x_train = Vectorizer.fit_transform(x_train)
y_train = transform(y_train)
# count=0
# for i in x_train:
#     print(type(i))
#     count+=1
#     if count==1:
#         break
import matplotlib.pyplot as plt
# plt.plot(x_train,y_train)
x_test = Vectorizer.transform(x_test)
y_test = transform(y_test)
pipeline = Pipeline([
    # ('tfidf', Vectorizer),
    ('classifier', RandomForestClassifier(n_estimators=500))
])
#
pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {round(accuracy*100,2)}%')
