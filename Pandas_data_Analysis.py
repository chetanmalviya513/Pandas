#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv("C:/Users/hp/Downloads/gapminder.csv")


# In[5]:


df


# In[6]:


print(df.head)


# In[7]:


df.head()


# In[9]:


df.shape


# In[10]:


df.columns


# In[13]:


df.dtypes


# In[15]:


print(df.dtypes)


# In[17]:


df.info()


# In[19]:


country_df = df["country"]
country_df


# In[21]:


country_df.head()


# In[22]:


country_df.tail()


# In[25]:


df.columns


# In[30]:


subset = df[["country","continent","year"]]
subset.head()


# In[32]:


print(subset.tail())


# In[33]:


print(df.loc[0])


# In[34]:


print(df.loc[99])


# In[35]:


df.head()


# In[36]:


print(df.loc[0])


# In[39]:


print(df.tail(n=1))


# In[41]:


print(df.loc[[0,99,999]])


# In[42]:


print(df.iloc[1])


# In[43]:


print(df.loc[1])


# In[44]:


print(df.iloc[-1])


# In[48]:


subset = df.loc[:,["year","pop",]]
subset.head()


# In[53]:


subset = df.iloc[:,[2,4,-1]]
subset


# In[65]:


small_range = list(range(5))
small_range


# In[68]:


subset = df.iloc[:,small_range]
subset.head()


# In[70]:


print(df.loc[45,["country"]])


# In[73]:


print(df.iloc[45,0])


# In[77]:


print(df.iloc[[0,99,999]])


# In[75]:


print(df.iloc[[0,99,999],[0,3,5]])


# In[83]:


print(df.loc[[1,100,555],["country","lifeExp","gdpPercap"]])


# In[86]:


print(df.loc[[0,122,555],["country","lifeExp","gdpPercap"]])


# In[93]:


print(df.loc[10:15],["country","lifeExp","gdpPercap"])


# In[94]:


print(df.head(n=10))


# In[95]:


print(df.groupby("year")["lifeExp"].mean())


# In[98]:


multi_group_var = df.groupby(["year","continent"])[["lifeExp","gdpPercap"]].mean()
multi_group_var


# In[99]:


flat = multi_group_var.reset_index()
flat.head(15)


# In[101]:


print(df.groupby("continent")["country"].nunique())


# In[103]:


global_yearly_life_expectancy = df.groupby("year")["lifeExp"].mean()
global_yearly_life_expectancy


# In[105]:


global_yearly_life_expectancy.plot( )

