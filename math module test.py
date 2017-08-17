import math  #importing the function we want to use


def pythag(sidea, sideb):    # defining the function pythag
    csquared = math.pow(sidea,2) + math.pow(sideb,2)  # using the math operator math.pow to show
                                                    # (number, raised to power)
    sidec = math.sqrt(csquared)                #using another math function math.sqrt to square out previous
                                               #answer from csquared to get the answer for our side c
    return sidec                               #the return function returns our answer for use later in our program so
                                               # so that we can output that variable to out def of pythag(sidea, sideb)

sidea = float(input("What is the length of side a"))  #asks the user for their input for the length of sidea
sideb = float(input("What is the length of side b"))  #asks the user for their input on the length of sideb

test1 = pythag(sidea, sideb)   #we set test1 equal to our definition of pythag(sidea, sideb)
print(test1) #we call print to print out the totals calculated from the def pythag(sidea, sideb that were
            # calculated.
