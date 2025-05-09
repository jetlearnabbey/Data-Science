import matplotlib.pyplot as plt

import numpy as np


marks = np.array([2,5,7,21])
labels = ["Maths","English", "Science","PE"]
explotion = [0,0,0,0.2]
colors = ["blue","cyan","yellow","maroon"]
plt.pie(marks,labels=labels,startangle=90,explode=explotion,shadow=True,colors=colors)
plt.show()
