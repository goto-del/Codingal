import sqlite3

database = "database.sqlite"

con = sqlite3.connect(database)
print("Open Data Succesfully!")

import pandas as pd

tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type = 'table';""",con)
print(tables)

matches = pd.read_sql("""SELECT * FROM Match;""",con)
print(matches)

matches.info()

match_wins = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner = 7;""",con)

print(match_wins)

teams = pd.read_sql("""SELECT * FROM Team;""",con)
print(teams)

details = pd.read_sql("""SELECT * FROM Team WHERE Team_Name LIKE 'D%';""",con)
print(details)

seasons = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 7 AND Season_ID IN (8,9);""",con)
print(seasons)

winners = pd.read_sql("""SELECT MIN(Win_Margin),MAX(Win_Margin) FROM Match;""",con)
print(winners)