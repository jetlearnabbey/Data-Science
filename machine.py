import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv("Data1.csv")

print(dataset.info())

#splitting into input and target
#print(dataset.iloc[:,1:3])

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
dataset.iloc[:,1:3]= imputer.fit_transform(dataset.iloc[:,1:3])
print(dataset.iloc[:,1:3])

ct = ColumnTransformer(transformers = [("encoder",OneHotEncoder(),[0])],remainder="passthrough")
dataset = ct.fit_transform(dataset)
print(dataset)




