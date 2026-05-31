# Simple storage for one user account
stored_username = ""
stored_password = ""

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("\n--- Register ---")
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")

        # lenth check
        if len(username) < 3 or len(password) < 3:
            print("Username and password must be at least 3 characters long!")
        else:
            stored_username = username
            stored_password = password
            print("Registration successful!")

    elif choice == "2":
        print("\n--- Login ---")
        if not stored_username:
            print("No accounts registered yet. Please register first.")
            continue

        username_input = input("Username: ")
        password_input = input("Password: ")

        # Validation check
        if username_input == stored_username and password_input == stored_password:
            print("Success! You are logged in.")
        else:
            print("Wrong username or password.")

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")

