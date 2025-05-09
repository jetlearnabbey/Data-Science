import matplotlib.pyplot as plt

engmarks = [50, 49, 47, 48]


mathmarks = [50,45,44,2]


scimarks = [49,46,43,39]


pemarks = [50,48,47,49]

terms = ["term1","term2","term3","term4"]
plt.stackplot(terms,engmarks, mathmarks, scimarks, pemarks, colors = ["red","orange","yellow","green"],labels=["English","Maths","Science","PE"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Bryan's Scores")
plt.show()





