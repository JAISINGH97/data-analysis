#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Data analysis


# In[1]:


import pandas as pd


# In[5]:


df=pd.read_csv("Downloads/Weather Data.csv")


# In[6]:


df.head()


# In[8]:


df.shape


# In[10]:


df.index


# In[11]:


df.columns


# In[13]:


df.dtypes #to get datatype of each column


# In[19]:


df['Weather'].unique()


# In[21]:


df.nunique() #to get unique values in each columns


# In[25]:


df.count() #it shows total number of non-null vales


# In[28]:


df.info()


# In[40]:


df['Weather'].value_counts()


# # find all the uniquevalues

# In[46]:


df.nunique()


# # find all the unique 'wind speed' values

# In[48]:


df['Wind Speed_km/h'].nunique()


# In[49]:


df['Wind Speed_km/h'].unique()


# # find the number of times when 'weather is exactly clear'

# In[52]:


df.Weather.value_counts()


# In[55]:


#using flitering
df[df.Weather=='Clear']


# In[61]:


#groupby()
df.groupby('Weather').get_group('Clear')


# # find the number of times , when the wind speed was 4kms/h

# In[63]:


df[df['Wind Speed_km/h']==4]


# # find null values
# 

# In[65]:


df.isnull().sum()


# In[68]:


#rename the columns
df.rename(columns={'Weather':'Weather Condition'},inplace=True)


# In[73]:


#mean visibility
df.Visibility_km.mean()


# In[77]:


#SD of pressure
df.Press_kPa.std()


# In[78]:


#value of relative humudity in the data
df['Rel Hum_%'].var()


# In[83]:


#find all the instances where snow was recorded
#df.head(2)
df['Weather Condition'].value_counts()


# In[85]:


df[df['Weather Condition']=='Snow']#filtering


# In[89]:


#str.contains
df[df['Weather Condition'].str.contains('Snow')]


# In[106]:


#wind speed is above 24 and visibility is 25
df.head(2)
df.rename(columns={'Wind Speed_km/h' : 'Wind'},inplace=True)
df[(df['Wind Speed'] > 24) & (df['Visibility_km'] == 25)]


# In[108]:


#mean value of each column against weather consition
df.groupby('Weather Condition').mean()


# In[109]:


#min and max value of each col. against each weather consition columns
df.groupby('Weather Condition').min() #replace max.()


# In[112]:


#show all the records where weather condition is Fog
df[df['Weather Condition']=='Fog']


# In[116]:


#weather condition is clear and visibility is above 40
(df['Weather Condition']=='Clear') | (df['Visibility_km']>40)


# In[121]:


#weather is clear and relative humidity is 50
#or visibility above 40
df[(df['Weather Condition']=='Clear') & (df['Rel Hum_%']>50)|(df['Visibility_km']>40)]


# In[ ]:




