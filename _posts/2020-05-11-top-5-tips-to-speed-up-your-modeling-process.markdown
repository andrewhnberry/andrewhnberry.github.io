---
layout: post
title: 04-Top 3 Tips to Speed up Your Modeling Process
excerpt: Your model is taking too long? Read this article!
date: '2020-05-11 14:59'
tags:
  - Data Science
  - Python
categories:
  - Data Science
---

The other day I was working on a brand new data science portfolio project (_link to the work in progress Github repository_ [_here_](https://github.com/andrewhnberry/Identifying-bad-debt)) and I was quite frustrated on how much time I was wasting, on waiting for the damn jupyter code cell to run! I'm sure some you can relate, or maybe you have more patience than me. It's annoying when you're doing something simple and you got to wait 10-15 minutes, or you're trying to test our your models but then after 30 minutes it spits out an error. With errors, when fixing you really want to a speedy validation of your fix, and not have to wait 30 minutes for it to spit another error.

**Overall, this is a sign that the dataset you are working with is just too big for your machine to handle.** If you're wondering, I'm using a 2016 15" MacBook Pro with the touchbar. Question to y'all reading this and have a version of a MacBook with a touchbar. Do y'all ever use it? Do you like it? Please reach out to me with your opinion. Anyways...let's get back to topic.

At least for me, whenever I'm doing a portfolio project when building out the code and modeling I would rather have a speedy execution as my proof of concept and have that all set up. Before I have my model take on the big data.

In this blog post, I will outline **3 easy tips to speed up your data science code execution process**.

### Tip 1: Sample your data
Probably the first thing I would do if things are taking a bit longer than usual. I would take a sample of my data. Generally, I use Pandas Dataframes to work with my data. It's great that they do have a built in sampling function. I'll show you below on how to use the function.

```python
import pandas as pd

#load in the dataset
df = pd.read_csv('data/loan.csv')

#Option 1: Where n = # of rows
df_subset = df.sample(n=10000, random_state = 42)

#Option 2: Where frac = fraction of the dataset you want to get
df_subset_2 = df.sample(frac = 0.3, random_state = 42)

#Option 3: Sampling with replacement
df_subset_3 = df.sample(frac = 0.3, replace = True)

````
Do note that opting to sample with replacement takes a bit longer. **I usually like to go with option 2**, and specify a fraction instead of a number of rows.

### Tip 2: Turn on n_jobs if you're using sklearn.
I don't know about you, but I normally do most of my modeling with the Sklearn package. I prefer it, I'm familiar with it, and it's great. It does have a feature that I believe is overlooked sometimes, I remember when I was a data science teacher assistant I used to tell my students to keep this feature on in order to  speed up their processing times. It usually enabled when calling the model.

You can specify n_jobs to a specific number like 2, which will then tell your model to use two cores. It you specify n_jobs to -1, it will tell your system to use all available cores. Thus, if your computer has 8 cores, it will use all 8 cores. Which will tremendously speed up computing with parallel computing. Often overlooked, and should be turned on.

```python
from sklearn.linear_model import LogisticRegression

# Use n_jobs = -1 to tell the model to use all of your system's CPU cores
log_reg_model = LogisticRegression(n_jobs = -1)

# Your Logistic Regression model will use two of your CPU cores
log_reg_model_1 LogisticRegression(n_jobs = 2)
```

### Tip 3: Dimensionality Reduction
Sometimes your dataset is large and there are many different features to take into account, which prolongs the computational time. Say you're doing a classic classification problem, most likely there are some features that are more important and relevant than other features. Some features may be weighted more than others by your model. Thus, why don't we take out the features that don't contribute to our model. The question then is, which features do we take out?

There are countless of dimensionality techniques, however I will show you how to use the  Principal component analysis (PCA) Dimensionality Reduction technique with Sklearn, which is one of my favourites and most popular.  I won't go into the details on the how PCA works, however, I will link you folks to a few great sources below.

1. https://setosa.io/ev/principal-component-analysis/
2. [StatQuest: PCA main ideas in only 5 minutes!!! by Josh Starmer](https://www.youtube.com/watch?v=HMOI_lkzW08)


Follow this code to your preferred python coding environment and play around to learn more on how to use PCA with Sklearn.
```python
#Importing the holy trinity of data science packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Our PCA from Sklearn
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

#Import the Dataset we will use
#We will use the digits dataset because it has the most features
#among all the practice datasets that sklearn provides
from sklearn.datasets import load_digits

#Loading our dataset
digits = load_digits()
X = digits.data
y = digits.target

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.33, random_state = 23)

#Instatiate the PCA model_selection
pca = PCA()

#Fitting the pca
pca.fit(X_train)
```
We've fit the instantiated and fit the PCA to our X_train. The PCA will then calculate the principal components which is a value that explains the percentage of explained variance for each principal component.

You can view the principal compoenents easily as it is stored as an array. To view, execute the code below/

```python
pca.explained_variance_ratio_
```
It will spit out this output:
```python
array([1.48170010e-01, 1.35868594e-01, 1.16822310e-01, 8.56309175e-02,
       5.88508205e-02, 4.89438957e-02, 4.43085909e-02, 3.78204714e-02,
       3.16836383e-02, 3.10840313e-02, 2.36661269e-02, 2.20943716e-02,
       1.88938982e-02, 1.78010981e-02, 1.47128367e-02, 1.37017660e-02,
       1.30327562e-02, 1.20879552e-02, 1.02940513e-02, 9.18011647e-03,
       8.65136221e-03, 8.11324311e-03, 7.65915745e-03, 7.29902522e-03,
       6.75057244e-03, 5.98691988e-03, 5.94495897e-03, 5.24465255e-03,
       4.68240350e-03, 4.28254535e-03, 3.79152547e-03, 3.55820014e-03,
       3.30783209e-03, 3.24997220e-03, 3.08522123e-03, 2.86344065e-03,
       2.57808105e-03, 2.36051351e-03, 2.21021891e-03, 2.19153579e-03,
       1.85557874e-03, 1.58926876e-03, 1.47379812e-03, 1.41074306e-03,
       1.14784958e-03, 1.13263407e-03, 9.52770886e-04, 6.55741370e-04,
       5.37262607e-04, 3.69155723e-04, 1.55315637e-04, 7.83941709e-05,
       5.65839210e-05, 5.03443976e-05, 4.52066897e-05, 1.72402656e-05,
       9.75708543e-06, 1.54371353e-06, 7.86547278e-07, 3.87270369e-07,
       1.68066241e-33, 7.85328965e-34, 7.85328965e-34, 7.54145401e-34])
```
Since the dataset we used had 64 feature, there are 64 principal components.

**From here there are two ways to interpret the prinicipal components to choose a cut off value on reducing the features in order to speed up computational time and preserve much of the explained variance of the dateset.**

#### Option 1:Plotting the explained variance ratio
```python
plt.figure(figsize = (14,7))
plt.plot(np.arange(1,65),pca.explained_variance_ratio_, marker = 'o', color = 'red')
plt.title('A PCA Graph', fontsize = 14)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Number of Principal Components (PCs)')
plt.xticks(np.arange(1,65,2))
plt.show()
```
![A PCA Graph](img/plots/pca_option1.png)
From here you want to a choose a value where you can start to notice diminishing returns for each principal component. For this graph you would choose a principal component of 15 or 17.

#### Option 2: Plotting the cumulative sum of the explained variance fraction
```python
plt.figure(figsize = (14,7))
plt.plot(np.arange(1,65), pca.explained_variance_ratio_.cumsum(), marker ='o', color = 'red')
plt.title('Cumulative Sum of PCA Graph')
plt.ylabel('Cumulative Sum of Percentage of Explained Variance')
plt.xlabel('Number of Principal Components (PCs)')
plt.xticks(np.arange(1,65,2))
plt.show()
```
![Cumulative Sum of PCA graph](img/plots/pca_option2.png)
In my opinion this a much easier plot to read.
