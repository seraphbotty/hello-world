#John Salazar
#8-14-17
#engr 120

def kinetic_energy():                                                       #calculation for kinetic energy is 1/2m*v^2
    m = int(input("What is the mass of the object in Kilograms? "))      #asks the user for an input on the mass of the
                                                                          #object
    v = int(input("How fast is the object traveling in meters per second? "))        #asks the user for the velocity or
                                                                                     #speed that the oject is traveling
    ke = 1 / 2 * m * v ** 2                                        #we are defining the formula that
                                                                   # will calculate the kinetic energy
                                                                  #that the object has as well as using the users input
    print("The kinetic Energy of the object is", ke)                  #printing the string in "" and then the output of
                                                                        #our calculation of ke described by our formula

kinetic_energy()                            #we then call the function we defined kinetic_energy()
                                            # so that the program can run the definition
                                            #we set as well as do the calculations and print the putput
