num = int(input("Enter a number between 0 and 12: "))

if num >= 0 and num <= 12:
    for i in range(13):
        print(i, "x", num, "=", i * num)
else:
    print("Invalid number! Please enter a number between 0 and 12.")