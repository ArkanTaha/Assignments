#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = (12,6)


# In[ ]:


df = pd.read_csv('driver-data.csv')
df.head()


# In[ ]:


df.info()


# In[ ]:


df.describe()


# In[ ]:


from sklearn.cluster import KMeans


# In[ ]:


kmeans = KMeans (n_clusters=2)
df_analyze = df.drop ('id', axis = 1)


# In[ ]:


kmeans.fit(df_analyze)


# In[ ]:


kmeans.cluster_centers_


# In[ ]:


print(kmeans.labels_)
print(len(kmeans.labels_))


# In[ ]:


print(type(kmeans.labels_))
unique, counts = np.unique(kmeans.labels_, return_counts = True)
print(dict(zip(unique, counts)))


# In[ ]:


df.analyze ['cluster'] = kmeans.labels_
sns.set_style('whitegrid')
sns.implot('mean_dist_day, mean_over_speed_perc, data = df_analyze, hue = 'cluster',
           palette = 'coolwarm', size = 6, aspect = 1, fit_reg = False)


# In[ ]:


kmeans_4 = KMeans(n_clusters = 4) 
kmeans_4.fit(df.drop('id', axis = 1))
kmeans_4.fit(df.drop('id', axis = 1))
print (kmeans_4.cluster_centers_)
unique, counts = np.unique(kmeans.labels_, return_counts = Ture)

kmeans_4.cluster_centers_
print(dict(zip(unique, counts)))


# In[ ]:


df.analyze ['cluster'] = kmeans_4.labels_
sns.set_style ('whitegrid')
sns.implot ('mean_dist_day, mean_over_speed_perc, data = df_analyze, hue = 'cluster',
           palette = 'coolwarm', size = 6, aspect = 1, fit_reg = False)

