import pickle

from sklearn import svm
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
St = pd.read_csv("FFCS_PREDICT.csv")
St1= St.drop('Pridicton' , axis='columns')
Training_Data= St1.drop('S No. ', axis='columns')
Pridiction_Value =St['Pridicton']
Labels = LabelEncoder()
# Training_Data1['Network_n'] = Labels.fit_transform(Training_Data(' Network'))
Training_Data['Network_n'] =pd.Categorical(Training_Data['Network']).codes
Training_Data['punctuality_n'] = pd.Categorical(Training_Data['punctuality']).codes
Training_Data['Gadget_conditon_n'] = pd.Categorical(Training_Data['Gadget_conditon']).codes
Training_Data['Health_n'] = pd.Categorical(Training_Data['Health']).codes
Training_Data['Disturbance_n'] = pd.Categorical(Training_Data['Disturbance']).codes
Training_Data['Friends_Help_n'] = pd.Categorical(Training_Data['Friends_Help']).codes
# vtop working or not
Training_Data = Training_Data.drop(['Network','punctuality','Gadget_conditon','Health','Disturbance','Friends_Help'],axis='columns')
print(Training_Data["Network_n"][:50:1])
# print(Training_Data)
Predictor = GaussianNB()
Training_Data = Training_Data.values
# print(Training_Data)
Predictor.fit(Training_Data,Pridiction_Value)
x_train,x_test,y_train,y_test = train_test_split(Training_Data,Pridiction_Value,test_size=.80)
Accuracy = Predictor.score(x_test,y_test)
# Predictor.
print("This program pridicts the chances of getting the course in FFCS of the vitap : ")
print("You only have to enter the condition of your present scenario")
Health = input("Is ur health good or bad => ").lower()
Network = input("Is ur Network connection good or bad => ").lower()
Punctuality = input("R u OnTime or Late => ").lower()
Gadget = input("Is ur Gadget condition Working or Not Working => ").lower()
Friends = input("Is ur Friends Helping yes of No => ").lower()
Disturbance = input("Is There any disturbance yes or no => ").lower()
try:
    if(Health=='good'):
        Health=1
    elif(Health=='bad'):
        Health = 0
    else:
        raise Exception('pls follow instruction and type accordingly')

    if(Network=='good'):
        Network=1
    elif(Network=='bad'):
        Network = 0
    else:
        raise Exception('pls follow instruction and type accordingly')
    if(Disturbance=='no'):
        Disturbance=0
    elif(Disturbance=='yes'):
        Disturbance = 1
    else:
        raise Exception('pls follow instruction and type accordingly')
    if(Friends=='yes'):
        Friends= 1
    elif(Friends=='no'):
        Friends=0
    else:
        raise Exception('pls follow instruction and type accordingly')
    if(Gadget=='working'):
        Gadget=1
    elif(Gadget=='not working' or Gadget=='notworking'):
        Gadget=0
    else:
        raise Exception('pls follow instruction and type accordingly')
    if (Punctuality == 'ontime'):
        Punctuality = 1
    elif(Punctuality=='late'):
        Punctuality = 0
    else:
        raise Exception('pls follow instruction and type accordingly')
except:
    print("pls type as instructed")


Pridiction = Predictor.predict([[Network,Punctuality,Gadget,Health,Disturbance,Friends]])

# Pridiction = Predictor.predict([[1,1,1,0,1,0]])
Final = Pridiction[0]
print(*Pridiction)
if(Final=='no'):
    print("No you cant do FFCS May God Bless Yo")
else:
    print("Yes you can do FFCS All The Best")
# Accuracy = Predictor.score(Training_Data,Pridiction_Value)
print("I am ",Accuracy*100,'% Sure about the prediction')
# print(Training_Data)
# pickle.dump(Predictor,open("my_model.pkl",'wb'))
