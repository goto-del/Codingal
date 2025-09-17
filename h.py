import pandas as pd

ceo = {"Name": ["Pankaj", "Meghna", "David", "Lisa"], "Role": ["CEO"], "Salary" : [100, 200]}

df = pd.DataFrame(ceo, index=["1", "2", "3", "4"])