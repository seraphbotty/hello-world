# CS/ENGR 120
# HMW_3 (while - loop)


# copyright © Lily Ma
# This file is for those who enrolled in Dr. Ma's class only
# Any unauthorized reproduction, distribution and modification
# of this file will be looked into.

#1
print("1.\n")
print()

counter = 1 # count number of iterations and control the loop

total = 0 # Accumulator

while counter <= 10:
    num = float(input("Enter your %d number:"% (counter))) # read in user input
    total = total + num # Add the input to total
    counter = counter + 1 # update counter
                        # so counter will be 1, 2, 3, ..., 10, loop repeats 10 times
                        
print("The total of your numbers is %d. " % (total))


input("\n\nEnd of problem 1. Press ENTER to continue.\n\n")

print('----------------------------------\n\n')


#2
print("2.\n\n")
day = 1
total = 0

while day <= 5: # Five days: day 1, 2, 3, 4, 5
    bugs = int(input("How many bugs collected on day %d" % (day)))
    while bugs < 0: # Check for input validation
        print("No negative numbers! ")
        bugs = int(input("Re-enter: "))
    total = total + bugs # add only the valid input to total 

    day = day + 1 # update counter

print("You collected %d bugs in five days"%(total))

input("\n\nEnd of Problem 2. Press ENTER to continue. \n\n")

print('-------------------------------------\n\n')


#3.
print("3. \n\n")

num = float(input("Enter a number:"))  
product = num * 10

while product < 100: # The condition that cause the loop to repeat is
                        # product should be less than 100
    print(num, " X 10 = ", product)
    num = float(input("Product is less than 100, enter another number: "))
    product = num * 10

print("Product exceeds 100. STOP!")    


input("\n\n End of Problem 3. Press Enter to continue. \n\n")

print('-----------------------------------------\n\n')

#4
print("4.\n\n")

from random import *

print("I shall randomly generate a number between one and ten. \
Think you can\nguess correclty?\
Go ahead and try,\nlets see how many tries it takes")


guess_c = 1   # Before the loop, user already guessed once, so here should be 1 not 0.

numb = randint(1,10)

guess = int(input("Guess a number between one and ten"))   # Here is the first try

while guess != numb: # When the guess is not the correct anwer, keep guess
    
    # the guess is either hogher or lower that the number
    # the if/else will check that and display a message accordingly 
    if guess >numb:   
                print("Too high, try again")

    elif guess < numb:
                print("Too low, try again.")

    # After one of the two messages displayed, user should be directed to
    # have a new guess
    guess = int(input("Try again. Pick a number between one and ten"))

    # user guessed one more time, add one to counter
    guess_c = guess_c + 1

# When user guessed the answer, 'guess!=numb' is false, loop stops
# Program execution continues on 
print("Correct!")   
print("Number of attempts:", guess_c)
