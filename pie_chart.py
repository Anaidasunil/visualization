#pip install matplotlib

import matplotlib.pyplot as plt

#data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]  # Proportions of the pie chart
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']  # Colors for each slice
explode = (0.1, 0, 0, 0)  # "Explode" the 1st slice (i.e. 'A')

# Create a pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title of the pie chart
plt.title('Sample Pie Chart')

# Display the plot
plt.show()
