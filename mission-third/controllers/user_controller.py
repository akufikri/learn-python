from models.user_model import insert_user,get_all_users

def add_user(name, email):
    try:
        insert_user(name, email)
        print(f"User {name} added successfully!")
    except Exception as e:
        print(f"Error adding user: {e}")

def fetch():
    try:
        users = get_all_users()
        return users
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []
