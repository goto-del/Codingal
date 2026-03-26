import sqlite3

database = "database.sqlite"

con = sqlite3.connect(database)

print("Open Data Succesfully")

import pandas as pd

tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type = 'table';""",con)

print(tables)

matches = pd.read_sql("""SELECT * FROM Match;""",con)
print(matches.tail())

winners = pd.read_sql("""SELECT AVG(Win_Margin) FROM Match WHERE Season_ID == 9;""",con)
print(winners)

seasons = pd.read_sql("""SELECT COUNT(DISTINCT Venue_ID) FROM Match WHERE Season_ID == 9;""",con)
print(seasons)

margins =pd.read_sql("""SELECT MIN(Win_Margin), Max(Win_Margin), Avg(Win_Margin), COUNT(DISTINCT(Man_of_the_Match))FROM Match;""", con)
print(margins)

season2 = pd.read_sql("""SELECT MIN(Win_Margin), Max(Win_Margin), Avg(Win_Margin), COUNT(DISTINCT(Man_of_the_Match))FROM Match WHERE Season_ID == 8;""", con)
print(season2)

total = pd.read_sql("""SELECT SUM(Win_Margin) FROM Match WHERE Season_ID == 9;""",con)
print(total)

aver = pd.read_sql("""SELECT AVG(Win_Margin),Match_Winner FROM Match WHERE Season_ID == 9 GROUP BY Match_Winner;""",con)
print(aver)