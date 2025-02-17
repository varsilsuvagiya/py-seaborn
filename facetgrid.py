import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")

# Create a FacetGrid with 'sex' as the row variable
g = sns.FacetGrid(tips, col="sex")

# Map a scatter plot to the grid
g.map(sns.scatterplot, "total_bill", "tip")

plt.show()
