import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

dataset = pd.read_csv("Data1.csv")

print(dataset.info())

#splitting into input and target
#print(dataset.iloc[:,1:3])

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
dataset.iloc[:,1:3]= imputer.fit_transform(dataset.iloc[:,1:3])
print(dataset.iloc[:,1:3])

