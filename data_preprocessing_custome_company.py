#in this only we handle the missingvalues
# coding: utf-8
#import neccessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read the csv data file using pandas

data=pd.read_csv("C:/data preprocessing/customers_company/data.csv")

#inspection of data
print(data.head())

#graphical representation of replation between each feature and label
x=data['Purchased']
for i in range(len(data.columns)-1):
    plt.figure(i+1)
    plt.plot(x,data[data.columns[i]],'gs')
    plt.ylabel(data.columns[i])
    plt.xlabel('Purchased')
    plt.grid()
    plt.show()

#data types of features in the data 
for i in data.columns:
    print(i+":",end=" ")
    print(data[i].dtype)
#alternate way to knowing the datatypes of features
#data.dtypes

#for knowing which features have missing values
for i in data.columns:
    print(sum(data[i].isnull()))

#handling missing values
for i in data.columns:
    data_type=data[i].dtype
    if(sum(data[i].isnull())>0):
        data[i].fillna(method='ffill',inplace=True)  

#after handling missing values
print(data)




