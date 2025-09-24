import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
print(df.head())

sns.distplot(df["petal_length"], hist = False)
plt.show()