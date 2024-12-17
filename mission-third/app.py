from controllers.user_controller import add_user, fetch
from views.use_view import showList, showMessage

def main():
    while True:
        print("\nMenu:")
        print("1. Add User")
        print("2. View Users")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            message = add_user(name, email)
            showMessage(message)
        elif choice == "2":
            users = fetch()
            showList(users)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()