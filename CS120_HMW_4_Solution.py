# CS/ENGR 120
# HMW _ 4 _ Solution
# This assignment is a practice of for-loop


# copyright © Lily Ma
# This file is for those who enrolled in Dr. Ma's class only
# Any unauthorized reproduction, distribution and modification of this file
# will be looked into.

# 1
print("1. \n")

print('''This program displays a multiplication table.
The table uses user input as one operand and number 1 to
10 as another operand.\n\n''')

user_num = int(input("Enter an integer, a multiplication table will generate for you : "))

# Since the program will use 1 throgh 10 sequentially, and display the exressions
# It should be a loop. We know the number of iterations is 10, 
# for-loop is the first choice
# while-loop works as well though.

for i in range(1, 11): # range(1, 11) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    print(user_num, " X ", i, " = ", user_num*i)   # The loop body has only one statement to perform
                                                    # the action
                                                    # which is displaying the expression.

                                                    
input("\n\n Press Enter to proceed to next problem.\n\n")

print('-------------------------------------------\n\n')

#2
print("2. \n\n")

print("This program counts how many even numbers and how many odd numbers\
are in a given list separately")

my_list = [2, 23, 34, 12, 56, 3, 66, 15, 89, 1, 123, 5, 90]

# We should take each number an check if the number is even or odd
# The operator to evaluate even or odd of a number is % operator
# if number % == 0: number is even
# else: number is odd.
# Instead of repeating the above codes for each number, we can use the loop
# to step through the list
# We have while loop and for-loop, two loop structures
# Since it is a list, we should use for-loop: loop through a sequence

# We need to count numbers, so we need counters.
even = 0  #counter for counting number of even numbers
odd = 0 # counyer for counting number of odd numbers

for i in my_list:
    if i%2 == 0: # i is an even number
        even = even + 1 # increase couner by 1
    else: # i must be an odd number
        odd = odd + 1 # increase odd counter by 1

# The following statements will only execute when for-loop terminates
# which means for loop stepped through the entire list
# you are ready to display your numbers

print("Number of even numbers: %d" % even)
print("Number of odd numbers: %d" % odd)


input("\n\n Press Enter to proceed to next problem.\n\n")

print('------------------------------------------------\n\n')


#3.
print("3.\n\n")

# This program reads in two emploees' hours
# and display the total and overall total

# Employee 1
num_emp = int(input("How many employees"))

overall = 0 #Accumulator for overall total

# Outer for-loop is for each employee
for employee in range(0, num_emp): #range function generates a list

    days = int(input("Emplyee %d: How many days?"%(employee+1)))

    total = 0 # the total hours for each employee

    # Inner for-loop is for each day of one employee
    for day in range(0, days): # == [0, 1, 2, ..., days-1]
        hrs = int(input("How many hours did you work on day %d?" % (day+1)))
        
        #input validation need to be placed here
        # think which are you gonna use: if or while
        # adjust your program accordingly
        
        total += hrs   # total1 = total1 + hrs
    print("Employee %d, you worked %d hours. \n" % (employee+1, total))

    overall = overall + total  # add individual total into overall total

# After all loops are finished, the overall total is ready to be displayed
# Note: it is outside the loop, NOT inside the loop!!

print("The %d employees worked %d hours in total.\n" % (employee, overall))




### Employee 2
##
##days = int(input("Emplyee 2: How many days?"))
##
##total2 = 0 # the total hours for employee 1
##
##for day in range(0, days): # == [0, 1, 2, ..., days-1]
##    hrs = int(input("How many hours?"))
##    total2 += hrs
##
##print("Employee 1, you worked ", total1 , "hours. \n")
##
    





