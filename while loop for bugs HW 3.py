#John Salazar
#while loop that adds user inputs for total bugs over 5 days
#then outputs the total bugs 
#7-31-17


day = 1
total = 0
print("Please enter the number of bugs caught for each day. ")

while day <= 5: #uses days 1 through 5
    #%d is for integer data type. They tell python to take the variable
    #on the right and put it in to replace the % with its value.
    bugs = int(input("Enter in how many bug you collected on day %d" % (day)))
    while bugs < 0:#set bugs total cant be a negative number
        print("No negative numbers please! ")
        bugs = int(input("Enter in for day: "))#has user enter a number for each day
    total = total + bugs# total starts at 0 and adds each days bugs to the total
    day = day +1# starts at 1 and adds 1 day to each new loop

print("You collected %d bugs in 5 days"%(total))#% sets the placeholder for days as the user input
                                                #for each days bug count
               
               
    
