import duckdb
conn = duckdb.connect()
data= conn.execute("""SELECT * FROM 'data/input.csv'""").fetchall()
print(data)