#By: Arkan Kabla

############


from mlxtend.data import iris_data
from mlxtend.preprocessing import standradize
from mlxtend.feature_extraction import LinearDiscriminantAnalysis


############


x, y = iris_data()
x = standardize(x)


############


lda = LinearDiscriminantAnalysis(n_discriminants=2)
lda.fit(x,y)
x_lda = lda.transform(x)


############

x_lda

