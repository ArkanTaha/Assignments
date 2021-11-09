import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = (12,6)


############

df = pd.read_csv('driver-data.csv')
df.head()


############

df.info()


############

df.describe()


############

from sklearn.cluster import KMeans


############

kmeans = KMeans (n_clusters=2)
df_analyze = df.drop ('id', axis = 1)


############

kmeans.fit(df_analyze)


############

kmeans.cluster_centers_


############

print(kmeans.labels_)
print(len(kmeans.labels_))


############

print(type(kmeans.labels_))
unique, counts = np.unique(kmeans.labels_, return_counts = True)
print(dict(zip(unique, counts)))


############

df.analyze ['cluster'] = kmeans.labels_
sns.set_style('whitegrid')
sns.implot('mean_dist_day, mean_over_speed_perc, data = df_analyze, hue = 'cluster',
           palette = 'coolwarm', size = 6, aspect = 1, fit_reg = False)


############

kmeans_4 = KMeans(n_clusters = 4) 
kmeans_4.fit(df.drop('id', axis = 1))
kmeans_4.fit(df.drop('id', axis = 1))
print (kmeans_4.cluster_centers_)
unique, counts = np.unique(kmeans.labels_, return_counts = Ture)

kmeans_4.cluster_centers_
print(dict(zip(unique, counts)))


############


df.analyze ['cluster'] = kmeans_4.labels_
sns.set_style ('whitegrid')
sns.implot ('mean_dist_day, mean_over_speed_perc, data = df_analyze, hue = 'cluster',
           palette = 'coolwarm', size = 6, aspect = 1, fit_reg = False)

