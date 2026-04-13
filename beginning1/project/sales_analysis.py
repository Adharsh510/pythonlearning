import pandas as pd
import sqlite3

# Load CSV into SQLite database
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
conn = sqlite3.connect("sales.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
print("Data loaded successfully")
print(df.columns.tolist())  # shows all column names