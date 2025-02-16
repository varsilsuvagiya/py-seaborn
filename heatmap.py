import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.rand(10, 10)  # 10x10 matrix

# Create the heatmap
sns.heatmap(data, cmap="coolwarm", annot=True, fmt=".2f")

# Show the plot
plt.show()
