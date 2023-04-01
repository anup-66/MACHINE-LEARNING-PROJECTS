import numpy
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
Data = pd.read_csv("spam.csv")
Data.drop('p1',axis=1,inplace=True)
Data.drop('p2',axis=1,inplace=True)
Data.drop('p3',axis=1,inplace=True)
# Replace the null values with a string
Modified_Data = Data.where((pd.notnull(Data)),'')
# print( Modified_Data.shape )

#sample data
# print(Modified_Data.head())

Modified_Data = Modified_Data.replace('ham',1)
Modified_Data = Modified_Data.replace('spam',0)
  # Or we can also use
  # Data.loc[Data['category']=='spam','category',]=0
  # Data.loc[Data['category']=='ham','category',]=1

Y = Modified_Data["Category"]
X = Modified_Data["message"]
x_train,x_test,y_train,y_test = train_test_split(X,Y,train_size=0.8,test_size=.2,random_state=3)

Equaliser = TfidfVectorizer(min_df = 1,stop_words = "english",lowercase = "True")
X_train_features = Equaliser.fit_transform(x_train)
X_test_features = Equaliser.transform(x_test)
# Use below lines when using the other methods line : 21 and 22
y_test = y_test.astype('int')
y_train = y_train.astype('int')

# training the data using svm as problem requires clustering that two binary features

model = LinearSVC()

# print(X_test_features,"         ")


# X_train_features1 = Equaliser.fit_transform([["Are you willing to go for aptitude class."]])

model.fit(X_train_features,y_train)
Prediction_training_data = model.predict(X_train_features)
Prediction_testing_data = model.predict(X_test_features)

# print(Prediction_testing_data)

accuracy_training_data = accuracy_score(y_train,Prediction_training_data)

print(accuracy_training_data)

# input_mail = [ "winner! chhutki is 100000000 very good i want to cuddle chhutki very tightly" ]
input_mail = [ "What are you waiting for? Hurry🕐Click below to get more details about this FREE webinar! Registrations for free CUET webinar are closing soon...⏰" ]
input_feature = Equaliser.transform(input_mail)
print(Equaliser.get_feature_names_out(),input_feature.shape)
prediction = model.predict(input_feature)
if prediction[0]==0:
    print("spam")
else:
    print("ham")