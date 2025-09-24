import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

print(df.head())

sns.displot(df["age"], kde=True)
plt.show()