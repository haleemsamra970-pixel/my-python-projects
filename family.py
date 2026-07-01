import random

# 1. الكمبيوتر يختار الرقم
secret_number = random.randint(1, 50)

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 50. Can you guess it?")

# 2. بدء اللعبة والمحاولات
guessed_correctly = False

while not guessed_correctly:
    user_guess = int(input("Enter your guess: "))
    
    # 3. مقارنة التخمين بالرقم السري
    if user_guess < secret_number:
        print("Bigger! The secret number is larger than that.")
    elif user_guess > secret_number:
        print("Smaller! The secret number is smaller than that.")
    else:
        print("🎉 Mabrook! The answer is correct, you guessed the number!")
        guessed_correctly = True # هنا نغير القيمة لتتوقف الحلقة وينتهي البرنامج