password = input("Enter your new password: ")

if len(password) >= 8 and len(password) <= 12:
    confirm_password = input("Enter your password again: ")

    if password == confirm_password:
        print("Password has been set!")
    else:
        print("Error: Passwords do not match!")
else:
    print("Error: Password must be between 8 and 12 characters!")