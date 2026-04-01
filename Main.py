import sqlite3

database = "database.sqlite"

con = sqlite3.connect('database.sqlite')

print("Open Data Succesfully")

con.execute("""CREATE TABLE CLASS_13
        (SNO INT PRIMARY KEY NOT NULL,
        Roll_No INT NOT NULL,
        Name TEXT NOT NULL,
        AGE INT DEFAULT (15),
        GENDER TEXT NOT NULL,
        Email_ID TEXT NOT NULL,
        Contact_No REAL NOT NULL);""")

print("Table Created Succesfully")

con.execute("INSERT INTO CLASS_13 VALUES (1, 1, 'Allen', 14, 'Male', 'allen@gmail.com', 8080900)");

con.execute("INSERT INTO CLASS_13 VALUES (2, 2, 'Aisha', 14, 'Female', 'aish@gmail.com', 9080900)");

con.execute("INSERT INTO CLASS_13 VALUES (3, 3, 'Jeff', 15, 'Male', 'allen@gmail.com', 9900900)");

con.commit()

print('Records Created Succesfully')

import pandas as pd

tables = pd.read_sql("""SELECT * FROM CLASS_13;""",con)
print(tables)

class_10 = pd.read_sql("""SELECT * FROM CLASS_13;""",con)
print(class_10.head())