username=input("Enter your username: ")
password=input("Enter your password: ")
match (username, password):
    case ("admin", "admin123"):
        print("Access granted. Welcome, admin!")
    case _:
        print("Access denied. Invalid credentials.")