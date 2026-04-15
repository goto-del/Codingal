import sqlite3
import pandas as pd
import numpy as np

database = "database.sqlite"

con = sqlite3.connect(database)

tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type = 'table';""",con)
print(tables)

player = pd.read_sql("""SELECT * FROM Player_Match;""",con)
print(player)

match_detail = pd.read_sql("""SELECT Season_Id,Match_Id,v.Venue_Name,c.City_Name,t.Team_Name AS winner FROM Match
                            INNER JOIN Venue AS v ON match.Venue_Id == v.Venue_Id
                            INNER JOIN City AS c ON v.City_Id == c.City_Id
                            INNER JOIN Team AS t ON match.Match_Winner == t.Team_Id;""", con)
print(match_detail)

