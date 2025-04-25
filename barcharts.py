import matplotlib.pyplot as plt
import numpy as np



x = np.array(["Maths","English","Science","Physical Education"])
y = np.array([1,12,11,2])
plt.title("Bob's Scores")
plt.barh(x,y,color="yellow",height=1.11)
plt.show()
