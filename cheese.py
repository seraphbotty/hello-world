# This program shows all the ways to get info to a function
def cheese_and_crackers(cheese, boxes_of_crackers):
    print ("You have %d cheeses!" % cheese) # %d is for an int variable
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    print ("Man that's enough for a party!")
    print ("Get a blanket.\n")

print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print ("OR, we can use variables from our scipt:")
amt_cheeses = 10
amt_crackers = 20

cheese_and_crackers(amt_cheeses, amt_crackers)

print ("OR we can get values from the user.")
cheese = int (input("How many cheeses? "))
boxes = int (input ("How many boxes of crackers? "))

cheese_and_crackers(cheese, boxes)
