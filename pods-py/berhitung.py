# Importing libraries
import numpy as np
import pandas as pd

# Generate random numbers
np.random.seed(101)
mat = np.random.randint(0,101,(100,5))

df = pd.DataFrame(mat, columns='A B C D Label'.split())

print(df.head())

# Import visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
import plotly.express as px

px.histogram(df, x='A',
			template='simple_white').show()



