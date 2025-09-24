import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("USA_Housing.csv")
print(df.head(10))

df.info()
df.describe()