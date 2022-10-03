# import numpy
# import random
# import matplotlib as plt
# import seaborn as sns
#
#
# def StudentRge(ages_train,net_worth_train):
#     from sklearn.linear_model import LinearRegression
#     reg = LinearRegression().fit(ages_train,net_worth_train)
#     return reg
#
#
# numpy.random.seed(1)
# ages = []
#
# for el in range(500):
#
#     ages.append(numpy.random.randint(18,75))
#
# NetWorth = [el*6.25 + numpy.random.normal(scale=40) for el in ages]
#
# ages = numpy.reshape(numpy.array(ages),(len(ages),1))
# NetWorth = numpy.reshape(numpy.array(NetWorth),(len(NetWorth),1))
#
# from sklearn.model_selection import train_test_split
#
# ages_train,ages_test,net_worth_train,net_worth_test = train_test_split(ages,NetWorth)
#
# reg1 = StudentRge(ages_train,net_worth_train)
# print("coefficient",*reg1.coef_)
# print("Intercept",*reg1.intercept_)
#
# print("Training_data",reg1.score(ages_train,net_worth_train))
# print("Test_data",reg1.score(ages_test,net_worth_test))
import random

import numpy as np
import random as rd
import sklearn as sk
import seaborn as sb
import matplotlib as mtp

def Stud(train_age,Net_worth_train):
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression().fit(train_age,Net_worth_train)
    return reg

age=[]
for r in range(500):
    age.append(random.randint(50,80))

# random.seed(1)
age = np.reshape(np.array(age),(len(age),1))
NetWorth = np.reshape(np.array([al*6.25 + np.random.normal(scale=40) for al in age]),(len(age),1))

from sklearn.model_selection import train_test_split

age_train,age_test,NetWorth_train,NetWorth_test = train_test_split(age,NetWorth)

reg1 = Stud(age_train,NetWorth_train)

print("Coefficient",reg1.coef_)
print("Intercept",reg1.intercept_)