By: Arkan Kabla

#####


import sklearn
from sklearn.datasets import load_iris


#####


data = load_iris()


#####


x = data.data
y = data.target


#####


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split (x, y, test_size = 0.2, random_state=1)


#####


print(x_train.shape)


#####


from sklearn.linear_model import LogisticRegression


#####


lr = LogisticRegression()


#####


lr.fit(x_train,y_train)


#####


y_predict = lr.predict(x_test)


#####


from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_predict, y_test)


#####


print(accuracy)


#####


from sklearn.decomposition import PCA 


#####


sklearn_pca = PCA(n_components = 0.95)


#####


sklearn_pca.fit(x_train)


#####


x_train_transformed = sklearn_pca.transform(x_train)


#####


print(x_train_transformed.shape)


#####


print(x_test.shape)


#####


x_test_transformed = sklearn_pca.transform(x_test)


#####


print(x_test_transformed.shape)


#####


print(x_test_transformed)


#####


lr = LogisticRegression(penalty='l2')


#####


lr.fit(x_train_transformed,y_train)


#####


y_predict = lr.predict(x_test_transformed)


#####


from sklearn.metrics import accuracy_score


#####


accuracy = accuracy_score(y_predict, y_test)
print(accuracy)


#####




