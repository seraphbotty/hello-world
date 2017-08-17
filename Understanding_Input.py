# Understand input( ) function
# The left side of the statement gets a value from the
# keyboard

# The right side of the assignment is a call to the function input()

# the input() function takes a string argument

# the input() function returns a string

food = input("What's your favorite food?")

'''When the user typed from keyboard and pressed the ENTER key,
input() RETURNS whatever the user tyoed as a string.
That string, the RETURN VALUE of the function call, is
the value stored in variable food.
'''

print("Ah, your favorite food is %s" % (food))

# The following code convert returned string into integer
# and then assign the integer to variable year

year = int(input('What year is it?'))

print("So next year will be ", year+1)

# The following code convert returned string to float
balance = float(input("What's your bank balance?"))
interest_rate = 0.001
print("Your interest will be ", balance * interest_rate)


