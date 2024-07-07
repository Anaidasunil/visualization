#pip install pandas statsmodels matplotlib
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

# Sample data
data = {
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male'],
    'Preference': ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A']
}

df = pd.DataFrame(data)

# Create a mosaic plot
fig, _ = mosaic(df, ['Gender', 'Preference'], title='Mosaic Plot Example')

plt.show()
