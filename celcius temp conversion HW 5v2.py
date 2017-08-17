#John Salazar
#8-14-17
#engr 120

def main():                               #defining the function we will use called main...(can be called anything)
    for i in range(21):                   #using the for loop to use a range of number.
                                          # can also set the for i as any variable
                                          #but must be cognizant to always use the
                                          #right naming convention throught program
        f = ((i - 32) * (5/9))            #setting f to the calculation needed to use the range of 0-20 and output the
                                          #temperatures in fehrenheit
        print(i, "\t", f)                          # after running the def main we are telling
                                          # the function to print the calculation of f

main()                                    #calling the function we have just defined allows
                                          # the output to be given for the function and ran. resulting
                                          # in the print command being issued and the
                                          #calculation for f being desplayed for 0-20