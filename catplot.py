import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")

# Create the factorplot
sns.catplot(x="sex", y="total_bill", hue="smoker", col="time", data=tips, kind="swarm", palette="Set1")

# Show the plot
plt.show()

