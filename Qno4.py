sweets = int(input("How many sweets are there? "))
pupils = int(input("How many pupils are present? "))

each_pupil = sweets // pupils
leftover = sweets % pupils

print("Each pupil will get", each_pupil, "sweets.")
print("There will be", leftover, "sweets left over.")