import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.boxplot(x="day", y="total_bill", hue="sex", data=tips,
            palette="Set3", flierprops={"marker": "o", "markerfacecolor": "red", "markeredgecolor": "black"},
            saturation=0.75, whiskerprops={"linewidth": 2}, capprops={"linewidth": 2})

plt.show()
