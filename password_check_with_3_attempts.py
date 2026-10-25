CORRECT_PASSWORD = "secret"
attempts_left = 3

while attempts_left > 0:
    password = input("Enter password: ")

    if password == CORRECT_PASSWORD:
        print("Access granted!")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Incorrect password. Attempts remaining: {attempts_left}\n")
        else:
            print("Access denied. Account locked.")
