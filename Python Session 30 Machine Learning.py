#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[9]:


df=pd.read_csv('winequality-red.csv')
df


# In[10]:


df.shape


# In[11]:


df.size


# In[13]:


df.columns


# In[16]:


df.info()


# # Summary Statistics

# In[18]:


df.describe()


# Exploring Data Variables

# In[19]:


df.quality.unique()


# In[20]:


df.quality.value_counts()


# # Data Visualizations

# In[22]:


sns.heatmap(df.isnull())


# In[23]:


dfcor=df.corr()


# In[25]:


dfcor


# In[27]:


sns.heatmap(dfcor)


# In[31]:


get_ipython().run_line_magic('pinfo', 'sns.color_palette')


# In[30]:


plt.figure(figsize=(6,4))
sns.heatmap(dfcor,cmap='Blues',annot=True)


# In[34]:


plt.figure(figsize=(10,6))
sns.heatmap(dfcor,cmap='YlOrRd_r',annot=True)


# # Ploting Outliers

# In[36]:


df.columns


# In[38]:


df['fixed acidity'].plot.box()


# In[39]:


df.plot(kind='box', subplots=True, layout=(2,7))


# In[44]:


sns.pairplot(df)


# In[45]:


df.drop('volatile acidity',axis=1,inplace=True)
df.head()


# # Removing Outliers

# In[48]:


from scipy.stats import zscore
z=np.abs(zscore(df))
z


# In[49]:


threshold=3
print(np.where(z>3))


# In[ ]:




