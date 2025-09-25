import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

print(df.head())

sns.pairplot(df, hue="species", palette="bright")
plt.show()