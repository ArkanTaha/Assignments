# DESCRIPTION 
This repository contains some of assignments such as: 'Data Wrangling', 'Supervised Learning', 'Unsupervised Learning', 'Features Engineering', 'Classification', 'Time Series Modeling', ' Ensemble Learning', 'Recommender Systems', and 'Text Mining'.

# Data Wrangling:
Description:

*Create a data frame consists of:
‘first_name’: ??, ‘last_name’: ??, ‘age’: ??, ‘preTestScore’:?? ,’postTestScore’: ??

*Objective: Perform data processing on the raw data.

*Actions to perform:
- Save the data frame into a .csv file as project.csv
- Read the project.csv file and print the data frame.
- Read the project.csv file without column heading.
- Read the project.csv file and make two index columns, namely, ‘First Name’ and ‘Last Name’.
- Print the data frame in a Boolean form as True or False. True for Null/ NaN values and false for non-null values.
- Read the data frame by skipping the first 3 rows and print the data frame.

# Features Reduction - LogisticRegression:
- import libraries and the dataset
- define the data and target values
- split the data and target values into training and testing sets
- implement a logistic regression model
- perform PCA transformation
- implement the logistic regression model over the transformed datasets
- check for the accuracy

# Labelled Feature Reduction:
- import libraries and the dataset
- define the data and target values
- instantiate LDA
- transform the x variables using LDA

# Fit the DicisionTreeClassifier and RandomForestClassifier:
- import libraries and the datasets
- preprocess the data using get dummies and label encoders
- impute the missing values using the most frequent values
- fit the decision tree classifier on the transformed data
- print the accuracy
- fit the random forest classifier on the transformed data
- print the accuracy of the random forest classifier model

# Fit SVM classifier - voice classification
- import the libraries and the datasets
- check for missing values
- check the distribution for the dataset
- preprocess the data using the label encoders
- fit SVM classifier on the transformed data
- print the accuracay, confusion metrics, and classification report
- use grid search to optimize the results further
- print the accuracay, confusion metrics, and classification report of the optimized model

# Cluster Animals:
- import libraries and the dataset
- check for missing values
- identify unique values and plot them
- extract features necessary for clustering within a single variable
- fit agglomerative clustering model on the feature data
- predict labels for each animal
- print the RMSE of the model

# Cluster Based Incentivization:
- import libraries and the dataset
- fit the K-means model on the dataset
- evaluate the cluster centers and labels
- plot the cluster to see the distribution of datapoints
- iterate the same by changing the number of clusters to 4
- again, evaluate the clusters to see the distribution of datapoints
- plot the cluster to see the distribution of datapoints
- draw inference out of both the plots
