import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset("fmri")

sns.lineplot(x="timepoint", y="signal", hue="event", data=fmri, palette="Set1")
plt.grid()
plt.show()
