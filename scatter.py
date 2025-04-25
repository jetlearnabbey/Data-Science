import matplotlib.pyplot as plt
import numpy as np


x =  np.array([5,7,10,13,4,2,1,15,12,11])
y =  np.array([80,93,96,97,81,85,84,83,89,99])
colors = np.array([0,10,20,30,40,50,60,70,80,90])
sizes = 20 *  np.array([5,7,20,13,4,2,30,15,12,11])

#making a scatter plot using x and y values


plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='nipy_spectral')
plt.show()
