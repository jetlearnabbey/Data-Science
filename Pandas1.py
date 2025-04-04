
import pandas as pd

#pandas series 
list1 = [1,2,3,4]
s1 = pd.Series(list1,index = ["a","b","c","d"])

studentid = {1:"Bob", 2:"John", 3:"Sam", 4:"Kyle"}

s2 = pd.Series(studentid)
print(s2)

print(s1["d"])
print(s1)

#making a data frame

data = {"Calories":[170,280,2001],"Duration":[10,23,50]}
df = pd.DataFrame(data)
print(df)

#how to locate different rows
print(df.loc[[0,1]])

#diabetes data set


df = pd.read_csv("diabetes.csv")
print(df.head(10))
print(df.tail(5))
print(df.info())
print(df.describe())














#isolating 1 row 
print(df[df.index==1])

#giving a range of rows
print(df[df.index.isin(range(2,10))])

#get the number of rows and columns 

print(df.shape)

#figuring out data based on the row and column

print(df.loc[5:10,"Insulin"])
print(df[["Glucose","BMI"]])
print(df.loc[100:110,["Glucose","BloodPressure","Outcome"]])

#conditional slicing

print(df[df.BloodPressure>100])
print(df.loc[df.BloodPressure>100,["Pregnancies","Glucose","BloodPressure"]])

#checking for missing values
print(df.isnull().sum())

#dropping null values/dropping the rows

df.dropna()




