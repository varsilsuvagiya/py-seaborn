import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.stripplot(x="day", y="total_bill", data=tips)

plt.show()
