import psycopg2

conn = psycopg2.connect(
    "dbname=snake_db user=postgres password=221177 host=localhost port=5432"
)

print("CONNECTED OK")
conn.close()