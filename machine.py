
import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


dataset = pd.read_csv("Data1.csv")

print(dataset.info())

#splitting into input and target
#print(dataset.iloc[:,1:3])

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
dataset.iloc[:,1:3]= imputer.fit_transform(dataset.iloc[:,1:3])
print(dataset.iloc[:,1:3])

ct = ColumnTransformer(transformers = [("encoder",OneHotEncoder(),[0])],remainder="passthrough")
dataset = ct.fit_transform(dataset)


#converting the dependent values using LabelEncoder

le = LabelEncoder()
dataset[:,-1] = le.fit_transform(dataset[:,-1])
print(dataset)
ss = StandardScaler()
dataset[:, 1:3]=ss.fit_transform(dataset[:, 1:3])
print(dataset)
X_train, X_test, y_train, y_test = train_test_split(dataset[:,3],dataset[:,-1],test_size=0.2,random_state = 50)
print(X_train)
print(X_test)
print(y_train)
print(y_test)


