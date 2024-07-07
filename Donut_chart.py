#pip install matplotlib
import matplotlib.pyplot as plt

# Sample data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]  # Proportions of the donut chart
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']  # Colors for each slice
explode = (0.1, 0, 0, 0)  # "Explode" the 1st slice (i.e. 'A')

# Create a pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Sample Donut Chart')

# Display the plot
plt.show()
