import random

print("🎯 Welcome to the Guess the Number Game!")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess (1–100): "))
    attempts += 1

    if guess < number:
        print("Too low! Try again ⬇️")
    elif guess > number:
        print("Too high! Try again ⬆️")
    else:
        print(f"🎉 Correct! The number was {number}. You guessed it in {attempts} tries!")
        break
