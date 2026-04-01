import sqlite3


database = "database.sqlite"

con = sqlite3.connect(database)

print("Open Data Succesfully")

import pandas as pd

df = pd.read_sql("""SELECT * FROM sqlite_master WHERE type = 'table';""",con)
print(df)

tables = pd.read_sql("""SELECT * FROM Player_Match;""",con)
print(tables.head)

nill = pd.read_sql("""SELECT * FROM Player_Match WHERE Team_ID IS NULL ;""",con)
print(nill)


matches = pd.read_sql("""SELECT * FROM Match;""",con)
print(matches.head)

nil = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner IS NULL ;""",con)
print(nil)