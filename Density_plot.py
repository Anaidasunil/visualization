#pip install pandas seaborn matplotlib

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    'Category': ['A']*15 + ['B']*15,
    'Value': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5,
              2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7]
}

df = pd.DataFrame(data)

# Create multiple density plots
sns.kdeplot(data=df, x='Value', hue='Category')

plt.title('Density Plot with Multiple Categories')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()

df = pd.DataFrame(data)

# Create a density plot
sns.kdeplot(data=df, x='Value')




# Show the plot
plt.title('Density Plot')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
