import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
titanic = sns.load_dataset("titanic")

# Create the count plot
sns.countplot(x="class", data=titanic)

# Show the plot
plt.show()
