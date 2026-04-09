import sqlite3
import pandas as pd
import numpy as np

database = "database.sqlite"

con = sqlite3.connect(database)

tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type = 'table';""",con)
print(tables)

countries = pd.read_sql("""SELECT * FROM country c;""",con)
print(countries)

city = pd.read_sql("""SELECT * FROM city ci;""",con)
print(city)

joint_city = pd.read_sql("""SELECT c.Country_Id,c.Country_Name,ci.City_Name
                         FROM country c
                         INNER JOIN city ci
                         ON c.Country_Id == ci.Country_Id;""",con)
print(joint_city)

players = pd.read_sql("""SELECT * FROM player;""",con)
print(players)

seasonss = pd.read_sql("""SELECT * FROM season;""",con)
print(seasonss)

joinout = pd.read_sql("""SELECT * FROM player LEFT JOIN season ON player.Player_Id == season.Man_of_the_Series;""",con)
print(joinout)

joincross = pd.read_sql("""SELECT c.Country_Id,c.Country_Name,ci.City_Name FROM country c CROSS JOIN  city ci;""",con)
print(joincross)