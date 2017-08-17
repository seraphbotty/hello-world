#John Salazar
#8-14-17
#engr 120

import random

def cointoss(times):       #passes 1 argument for the meaning of heads or tails.
                           #the argument passed will also be used in the variable for range.

    for i in range(times): #we set the variable we will pass what each heads or tails is defined

        c = random.randint(1,2) #lets the random numbers choosen be 1 or 2 as defined by random.randint

        if c == 1: # we define that if c is equivelent to 1 it is tails

            print("You flipped tails!") #output called

        else: #if the if statement is passed the else function is called.

            print("You flipped heads!") #output called

num = int(input("How many times do you wanna play? ")) #user is asked for input and the function is ran with
                                                      #the desired number of coin tosses

cointoss(num) #the function cointoss(num) is called and the function cointoss is ran with the users input
            #for how many times they would like to let the coin be tossed, the variable is in cointss(variable does
            #not matter ony that the required number of arguments are passed)

