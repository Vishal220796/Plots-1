import matplotlib.pyplot as plt


activities = ['eat', 'sleep', 'work', 'football', 'cycling', 'coding']


slices = [3, 9, 8, 6, 5, 7]


colors = ['orange', 'blue', 'green', 'maroon', 'yellow', 'aqua']


plt.pie(slices, labels = activities, colors=colors,
        startangle=30, shadow = True, explode = (0,0,0,0,0,0.2),
        radius = 1.2, autopct = '%3.3f%%')


plt.legend()


plt.show()

