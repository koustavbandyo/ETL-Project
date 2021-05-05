#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine
import csv


# In[2]:


pd.__version__


# In[3]:


df = pd.read_csv (r'C:\Users\13129\Desktop\Netflix.csv')


# In[4]:


print (df)


# In[5]:


hsif = pd.read_csv(r'C:\Users\13129\Desktop\Netflix.csv')
hsif.head()


# In[9]:


cols2skip=[4,6,9,10,11]


# In[11]:


cols=[i for i in range(12)if i not in cols2skip]


# In[12]:


cols


# In[13]:


df = pd.read_csv(r'C:\Users\13129\Desktop\Netflix.csv',usecols=cols)


# In[14]:


print (df)


# In[ ]:




