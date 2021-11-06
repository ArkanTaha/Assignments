#By: Arkan Kabla

#######################


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


#######################


df = pd.read_csv('voice-classification.csv')
df.head()


#######################


df.info()


#######################


df.describe()


#######################


df.isnull().sum()


#######################


print("shape of data: ", df.shape())
print("total number of labels: {}".format(df.shape[0]))
print("number of males: ".format(df[df.label=='male'].shape[0]))
print("number of females: ".format(df[df.label=='female'].shape[0]))


#######################


X = df.iloc[;, ;-1]
print(df.shape)
print(x.shape)


#######################


from sklearn.preprocessing import LabelEncoder


#######################


y = df.iloc[:, -1]

gender_encoder = LabelEncoder()
y = gender_encoder.fit_transform(y)


#######################


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x)
x = scaler.transform(x)


#######################


from sklearn.model_selection import train_test_spilt
x_train, x_test, y_train, y_test = train_test_spilt (x, y, test_size = 0.3, random_state = 100)


# In[ ]:


from sklearn.svm import SVC
from sklearn import metics
from sklearn.metrics import classification_report, confusion_metrix


#######################


svc_model = SVC()
svc_model.fit(x_train, y_train)
y_pred = svc_model.predict(x_test)


#######################


print('Accuracy Score: ')
print(metrics.accuracy_score(y_test, y_pred))


#######################


print(confusion_metrix(y_test, y_pred))


#######################


from sklearn.model_selection import GridSearchCV


#######################


param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001]}


#######################


grid = GridSearchCV(SVC(), param_grid, refit = True, verbose = 2)
grid.fit(x_train, y_train)


#######################


grid_predictions = grid.predict(x_test)


#######################


print('Accuracy Score: ')
print(metrics.accuracy_score(y_test, grid_predictions))


#######################


print(confusion_metrix(y_test, grid_predictions))


#######################


print(classification_report(y_test, grid_predictions))

