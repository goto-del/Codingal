import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
print(df.head())

sns.boxplot(x="class", y="age", data=df, palette="Set3")
plt.show()