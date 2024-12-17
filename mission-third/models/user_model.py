from database.user_database import connect

def insert_user(name, email):
    conn = connect()
    if conn:
        try:
            cur = conn.cursor()
            query = '''
            INSERT INTO users (name, email) VALUES (%s, %s);
            '''
            cur.execute(query, (name, email))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Error inserting user: {e}")
        finally:
            conn.close()

def get_all_users():
    conn = connect()
    if conn:
        try:
            cur = conn.cursor()
            query = 'SELECT id, name, email FROM users;'
            cur.execute(query)
            users = cur.fetchall()  # Hasil query berupa list of dictionaries
            cur.close()
            return users
        except Exception as e:
            print(f"Error retrieving users: {e}")
            return []
        finally:
            conn.close()
    return []