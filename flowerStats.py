import sys
import scipy
import numpy as np
import matplotlib as mb
import pandas as pd
import sklearn as sk
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#pulling the data from this file
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"

#creating the column head names
names= ['sepal-length', 'sepal-width','petal-length','petal-width','class']
#iris data stores the names of the parameters of the folowers

#creating the dataset
dataSet = read_csv(url, names=names)
#printing and organizing the dataset
print("\nThe data set 'shape' is: {}".format(dataSet.shape))
print("\nThis is the head of the data set:")
# head shows the first 20 of the dataset
print(dataSet.head(20))
print("\nHere is statistical information about the data set")
print(dataSet.describe())
#groups data
print("\nGrouping the data by: ")
print(dataSet.groupby('class').size())

#visualize dataset
dataSet.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()


dataSet.hist()
pyplot.show()
#splitting up the data to test and train from. 20% is used for testing. 80 percent is used for training
array = dataSet.values
x = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation, = train_test_split(x, y, test_size=0.2, random_state=1 )


#getting all the models we need for this project and putting them in the list called models
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

print('\nResults of testing each model against the data')
results = []
names = []
for name, model in models:
  kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
  cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
  results.append(cv_results)
  names.append(name)
  print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))


pyplot.boxplot(results, labels=names)
pyplot.title('algorithm comparison')
pyplot.show()
