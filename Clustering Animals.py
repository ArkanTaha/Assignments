import pandas as pd

data = pd.read_csv("zoo.csv")

data.info()

import numpy as np
labels = data['class_type']
print(np.unique(labels.values))

from matplotlib import pyplot as plt
%matplotlib inline
fig, ax = plot.subplots()
(labels.values_counts()).plot(ax=ax, kind = 'bar')

data.head()

features = data.values [:, 1:-1]
features.shape()

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances

model = AgglomerativeCulstering(n_clusters = 7, linkage = "average", affinity = "cosine")

model.fit(features)

model.labels_

print(np.unique(model.labels_))

labels = labels -1

from sklearn.metrics import mean_squared_error

score = mean_squared_error(labels, labels_)

abs_error = np.sqrt(score)
print(abs_error)

