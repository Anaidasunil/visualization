#pip install pandas plotly
import pandas as pd
import plotly.express as px


data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [2, 3, 4, 5, 6],
    'Feature3': [5, 4, 3, 2, 1],
    'Feature4': [6, 7, 8, 9, 10],
    'Class': ['A', 'A', 'B', 'B', 'C']
}

df = pd.DataFrame(data)

# Map class labels to numerical values
class_mapping = {label: idx for idx, label in enumerate(df['Class'].unique())}
df['ClassNum'] = df['Class'].map(class_mapping)

fig = px.parallel_coordinates(
    df,
    color='ClassNum',
    dimensions=['Feature1', 'Feature2', 'Feature3', 'Feature4'],
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=1
)

fig.show()

