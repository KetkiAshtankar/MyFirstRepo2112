import random

number = (random.randint(1,100))
print(number)
attempts = 0

print("Guess the number between 1 and 100 !!!!!!")

while True:
    guess = int(input("Enter your guess:"))
    attempts += 1

    if guess > number:
        print("Too high. try again")
    elif guess < number:
        print("Too low. try again")
    else:
        print(f"Congratulation!!!, you guessed correct number in {attempts} attempts")

        break


