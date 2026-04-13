import pandas as pd
import sqlite3

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
conn = sqlite3.connect("sales.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

print ("=== Total Sales by Country ===")
# query1 = pd.read_sql_query("SELECT COUNTRY, ROUND(SUM(SALES), 2) AS TOTAL_SALES " \
# "FROM sales" \
# " GROUP BY COUNTRY" \
# " ORDER BY TOTAL_SALES DESC", conn )
# print(query1)

# query2= pd.read_sql_query("SELECT PRODUCTLINE, ROUND(SUM(SALES), 2) AS TOTAL_SALES " \
# "FROM sales " \
# "GROUP BY PRODUCTLINE " \
# "ORDER BY TOTAL_SALES DESC", conn )
# print(query2)

# query3 = pd.read_sql_query("SELECT MONTH_ID, ROUND(SUM(SALES), 2) AS TOTAL_SALES " \
# "FROM sales " \
# "GROUP BY MONTH_ID " \
# "ORDER BY TOTAL_SALES DESC", conn )
# print(query3)
# query4 = pd.read_sql_query("SELECT DEALSIZE, ROUND(SUM(SALES), 2) AS TOTAL_SALES, COUNT(*) AS TOTAL_ORDERS " \
#  "FROM sales " \
# "GROUP BY DEALSIZE " \
# "ORDER BY TOTAL_SALES DESC", conn)
# print(query4)

query5 = pd.read_sql_query("""
    SELECT CUSTOMERNAME, ROUND(SUM(SALES), 2) AS TOTAL_SALES
    FROM sales
    GROUP BY CUSTOMERNAME
    ORDER BY TOTAL_SALES DESC
    LIMIT 5
""", conn)
print(query5)