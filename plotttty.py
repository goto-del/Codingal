import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
print(df.head())

sns.lmplot(x="petal_length", y="sepal_length", data=df, palette="pastel")
plt.show()