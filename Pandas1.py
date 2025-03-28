import pandas as pd

#pandas series

'''list1 = [1,2,3,4]
s1 = pd.Series(list1,index = ["a","b","c","d"])

studentid = {1:"Bob", 2:"John", 3:"Sam", 4:"Kyle"}

s2 = pd.Series(studentid)
print(s2)

print(s1["d"])
print(s1)'''

#making a data frame

'''data = {"Calories":[170,280,2001],"Duration":[10,23,50]}
df = pd.DataFrame(data)
print(df)

#how to locate different row
print(df.loc[[0,1]])'''

#diabetes data set


df = pd.read_csv("diabetes.csv")
print(df.head(10))
print(df.tail(5))
print(df.info())
print(df.describe())




