import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

sns.jointplot(x = "petal_length", y = "petal_width", data = df)
plt.show()