password = input("Enter your password here: ")
strength = 0
if len(password) >= 8:
    strength += 1
if any(char.isdigit() for char in password):
    strength += 1
if any(char.isalpha() for char in password):
    strength += 1    

if strength == 3:
    print("Your password is strong.")
elif strength == 2:
    print("Your password is medium.")    
else:
    print("Your password is weak.")    