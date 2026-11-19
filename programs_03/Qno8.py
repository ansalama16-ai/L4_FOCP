num = int(input("Enter a number: "))

if num >= 0:
    for i in range(13):
        print(i, "x", num, "=", i * num)
else:
    for i in range(12, -1, -1):
        print(i, "x", abs(num), "=", i * abs(num))