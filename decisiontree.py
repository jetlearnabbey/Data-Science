import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

dataset = pd.read_csv('iris.xlsx', names=['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'])


print(dataset.info())


#le = LabelEncoder()
#dataset.iloc[:, -1] = le.fit_transform(dataset.iloc[:, -1])


print(dataset.head())





X=dataset.drop('Species')
y=dataset["Species"]    
print(X.head())
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)

model = DecisionTreeClassifier(max_depth=3, random_state=1)

model.fit(X_train,y_train)
predictions = model.predict(X_test)
print("Accuracy: ",metrics.accuracy_score(predictions, y_test))

