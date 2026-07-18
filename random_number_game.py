import random

guess = int(input("Enter a random number between 1 and 6: "))

number = random.randint(1,6)
print(number)

if guess == number: 
    print("You win")
else: 
    print("Better luck next time")