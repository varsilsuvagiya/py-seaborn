import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.barplot(x="sex", y="total_bill", hue="smoker", data=tips, palette="Set1")
plt.grid()
plt.show()