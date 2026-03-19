import sqlite3

database = 'database.sqlite'
connection = sqlite3.connect(database)
print("Open Data Sucessfully.")

import pandas as pd

tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type = 'table';""",connection)
print(tables)