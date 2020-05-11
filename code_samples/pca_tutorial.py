#Importing the holy trinity of data science packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Our PCA from Sklearn
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split


#Import the Dataset we will use
#We will use the digits dataset because it has the most features among all
#the practice datasets that sklearn provides
from sklearn.datasets import load_digits


#Loading our dataset
digits = load_digits()
X = digits.data
y = digits.target

#Our dataset has 1797 rows and 64 features
X.shape

#We have a datset of images of number, why not display one of them.
plt.matshow(digits.images[0])

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.33, random_state = 23)

#Instatiate the PCA model_selection
pca = PCA()

#Fitting the pca
pca.fit(X_train)
#X_train = pca.transform(X_train)

pca.explained_variance_ratio_
len(pca.explained_variance_ratio_)

explained_variance_ratio_list = pca.explained_variance_ratio_

#Ploting PC

plt.figure(figsize = (14,7))
plt.plot(np.arange(1,65),pca.explained_variance_ratio_, marker = 'o', color = 'red')
plt.title('A PCA Graph', fontsize = 14)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Number of Principal Components (PCs)')
plt.xticks(np.arange(1,65,2))
plt.show()

#Interprate the model_selection


#Option 2


plt.figure(figsize = (14,7))
plt.plot(np.arange(1,65), pca.explained_variance_ratio_.cumsum(), marker ='o', color = 'red')
plt.title('Cumulative Sum of PCA Graph', fontsize = 14)
plt.ylabel('Cumulative Sum of Percentage of Explained Variance')
plt.xlabel('Number of Principal Components (PCs)')
plt.xticks(np.arange(1,65,2))
plt.show()

#From here you can choose the number of componenets.
new_pca = PCA(n_components = 13)
new_pca.fit(X_train)

X_train = new_pca.transform(X_train)
X_test = new_pca.transform(X_test)
