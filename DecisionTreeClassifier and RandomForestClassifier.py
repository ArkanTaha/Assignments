#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plot
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


animals = pd.read_csv("horse.csv")


# In[ ]:


target = animals ['outcome']


# In[ ]:


target.unique()


# In[ ]:


animals = animals.drop(['outcome'], axis = 1)


# In[ ]:


category_variables = ['surgery', 'age', 'temp_of_extremities', 'peripheral_pulse', 
                     'mucouse_membrane', 'capillary_refill_time', 'pain', 'peristalsis',
                     'abdominal_distention', 'nasogastric_tube', 'nasogastric_reflux', 
                      'rectal_exam_feces', 'abdomen', 'abdomo_appearance', 'surgical_lesion',
                     'cp_data']
for category in category_variables:
    animals[category] = pd.get_dummies(animals[category])


# In[ ]:


from sklearn.model_selection import train_test_spilt
from sklearn.preprocessing import LabelEncoder

x,y = animals.values, target.values

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

x_train, x_test, y_train, y_test = (train_test_spilt(x, y, test_size=0.2, random_state=1))


# In[ ]:


from sklearn.tree import DecisionTreeClassifier
print (x_train.shape)


# In[ ]:


from sklearn.preprocessing import imputer
imp = imputer(missing_values = "NaN", strategy = "most_frequent", axis = 0)
x_train = imp.fit_transform(x_train)
x_test = imp.fit_transform(x_test)


# In[ ]:


classifier = DecisionTreeClassifier()


# In[ ]:


classifier.fit(x_train, y_train)


# In[ ]:


y_predict = classifier.predict(x_test)


# In[ ]:


from sklearn.metrics import accuracy_score


# In[ ]:


print(accuracy)


# In[ ]:


from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()


# In[ ]:


classifier.fit(x_train, y_train)
y_predict = classifier.predict(x_test)
accuracy = accuracy_score(y_predict, y_test)
print(accuracy)

