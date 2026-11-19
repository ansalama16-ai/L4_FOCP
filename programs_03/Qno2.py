password = input("Enter your new password: ")
confirm_password = input("Enter your password again: ")

if password == confirm_password:
    print("Password has been set!")
else:
    print("Error: Passwords do not match!")