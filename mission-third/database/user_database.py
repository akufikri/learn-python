import psycopg2
from psycopg2 import sql, extras

def connect():
    try:
        conn = psycopg2.connect(
            database="BASIC",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        conn.cursor_factory = extras.DictCursor
        return conn
    except Exception as x:
        print("Error: {x}")
        return None