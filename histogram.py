import matplotlib.pyplot as plt
import numpy as np


'''x = np.random.normal(170,10,250)
print(x)
plt.hist(x)
plt.show()'''
ages = [5,6,7,8,9,10,25,2,13,17,20,14,61,87]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(ages,bins,histtype="bar")
plt.title("Ages and Bins")
plt.show()
