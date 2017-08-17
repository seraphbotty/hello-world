#John Salazar
#7-31-17
#Program asks for user input and makes a random number between 1-10
#add up your tries and tell you how many tries it took after you
#guess correctly

import random

number = random.randint(1, 10)
guess = int(input("Enter a number between 1 and 10"))
count = 1


while guess != number:
    if guess > number:
        print("Your number is to high, Please enter another number to try again")
    elif guess < number:
        print("Your number is to low, Please enter another number to try again")

    guess = int(input("Try again. Pick a number between 1 and 10"))
    count = count + 1

print("Correct!")
print("Number of attempts", count)
