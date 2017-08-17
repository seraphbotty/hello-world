# CS/ENGR 120
# HMW_2 Solution
# copyright © Lily Ma
# This file is for those who enrolled in Dr. Ma's class only
# Any unauthorized reproduction, distribution and modification
# of this file will be looked into.


"""
++++++++++++++++++++++++++++++++++++++++++++++++
Discussion:                                    +
1. Using while to write user-controlled loop;  + 
2. Using while-loop for user input validation. +
++++++++++++++++++++++++++++++++++++++++++++++++
"""

#Problem 1

print("1. \n\n")

print("Presented with two numerical values, i am able to \ndetermine which is greater, which is lesser,\nor if they are equal.")

num = int(input("\nPlease enter in a numerical value."))


num_2 = int(input("\nPlease enter in another numerical value."))

if num > num_2:
    print(num, "is greater than", num_2,"while",num_2, "is smaller than", num)
    

elif num_2 > num:
    print(num_2, "is greater than", num,"while",num,"is smaller than",num_2)
    
else:
    print("Both values are equal")

input("End of program. Press Enter to proceed to next program.")
print('\n\n-----------------------------------\n\n')



#Problem 2
print('2. \n\n')

print("Hello, at Software Giant we stock a special package that retails for $99.\n\
Based on the quantity of your purchase, you may be eligible for a discount.\n\
That's where i come in!!!!!!.")


quantity = int(input("\nPlease enter the number of packages you plan to purchase"))

# Set up variables
unit_price = 99
dis_rate = 0 # Rate of discount
discount = 0  # amount of discount 
cost = 0        

if quantity < 0: # Validate user input
    print("Sorry, quantity can not be negative values.")
else:  # deside the discount
    if quantity < 10:
        dis_rate = 0
        
    elif quantity < 20:
        dis_rate = 0.2
        
    elif quantity < 50:
        dis_rate = 0.3
    
    elif quantity < 99:
        dis_rate = 0.4
        
    elif quantity >=100:
        dis_rate = 0.5

    # The following calculations and outputs
    # should be inside the else-clause

    cost = quantity*unit_price  # cost without discount
    discount = cost * dis_rate # total discount
    final = cost - discount # final cost with discount

    print("Based on your purchae you get a ", dis_rate*100, "% discount.")
    print("Your total cost is $", final)
    print("You saved $%d on this purchase!" % discount) 

input("\n\n End of program. Press Enter to proceed to the next program.\n\n")

print('--------------------------------------------------\n\n')


#Problem 3

print("Geometry Calculator")

print("\n\t1. Calculate the Area of a Circle")

print("\n\t2. Calculate the Area of a Rectangle")

print("\n\t3. Calculate the Area of a Triangle")

print("\n\t4. Quit")

import math

num = int(input("\n\tEnter your choice (1-4): "))

while num != 4:  # Use a while loop to let the user deside calcultate another set
                    # or not
    if num == 1:
        print("Given the radius of a circle, we are able to calculate the area of a circle.")
        r = int(input("What is the radius of this circle(in inches)? "))
        print("Ok calculating.......")
        print("The area of the circle is",round(math.pi * r ** 2,2),"inches squared")
        
        
    elif num == 2:
        
        print("Given the length and width of a rectangle,\nwe can calculate the area of that rectangle.")
        l = int(input("What is the length of the rectangle(in inches)? "))
        w = int(input("What is the width of the rectangle (in inches)? "))
        print("Ok calculating........")
        print("The area of the rectangle is", l * w, "inches squared.")


    elif num == 3:

        print("Given the length of a triangle's base and height\nwe can calculate it's area.")
        b = int(input("What is the base length of the triangle (in inches)? "))
        h = int(input("What is the height of the triangle (in inches)? "))
        print("Ok calculating.......")
        print("The area of the triangle is",round(b * h * 0.5,2), "inches squared.")

    # Ask if the user wants to calculate another set    
    num = int(input("\n\n Do you wanna continue?\
    Choose 1-3 to calculte another area, or choose 4 to quite: "))

# When user choose 4    
input("\n\nYou choose to quit the program. Press ENTER to quit. Thanks!")

print('----------------------------\n\n')



#Problem 4

print('4. \n\n')

print("Hello! At Serendipity Booksellers we have a bookclub that awards points\n\
to its customers based on the amount of books purchased each month")

book = int(input("Please enter the amount of books you have purchased this month\n\
                 and i can determine the amount of points to award your account.\n\
                 Number of books bought? -- "))

points = 0 
if book == 0:
    points = 0

elif book == 1:
    points = 5

elif book ==2:
    points = 15

elif book ==3:
    points = 30
    
elif book >=4:
    points = 60
   
print("Ok calculating........")
print("This month you are awarded %d points." % points)

input("Thank you for your purchases! Unless you bought none\nto which i am dissapointed.")

    
       
