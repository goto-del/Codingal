import sqlite3
import pandas as pd
import numpy as np

database = "database.sqlite"

con = sqlite3.connect(database)

tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type = 'table';""",con)
print(tables)

team = pd.read_sql("""SELECT * FROM Team;""",con)
print(team)

season = pd.read_sql("""SELECT * FROM Season ;""",con)
print(season)


csk_matches_2015 = pd.read_sql("""SELECT Match_Id, Team_2 as Away_Team, Toss_Winner, Match_Winner
                            FROM Match 
                            WHERE Team_1 = 
                            (SELECT Team_1
                            FROM Match
                            WHERE Team_1 == 3 AND Season_Id == 8)""", con)

print("Matches Played By Chennai Super Kings in Year 2015")

k = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 3 AND Season_Id == 8;""",con)
print(k)