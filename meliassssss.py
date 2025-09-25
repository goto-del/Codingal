import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
print(df.head())

sns.scatterplot(x="flipper_length_mm", y="body_mass_g", hue="species", data=df)

plt.title("Penguin Flipper Length vs Body Mass")
plt.show()