
# coding: utf-8

# In[1]:


import pandas as pd


# In[60]:


data=pd.read_csv("C:/data preprocessing/customers_company/data.csv")


# In[61]:


data


# In[74]:


for i in data.columns:
    print(i+":",end=" ")
    print(data[i].dtype)    
#data.dtypes


# In[63]:


for i in data.columns:
    data_type=data[i].dtype
    if(sum(data[i].isnull())>0):
        if(data_type!='object'):
            data[i].fillna(data[i].median(),inplace=True)  


# In[64]:


data


# In[65]:


import matplotlib.pyplot as plt


# In[75]:


x=data['Purchased']
for i in range(len(data.columns)-1):
    plt.figure(i+1)
    plt.plot(x,data[data.columns[i]],'gs')
    plt.ylabel(data.columns[i])
    plt.xlabel('Purchased')
    plt.grid()
    plt.show()

