#John Salazar
#7-31-17
#This program uses a while loop to allow the user to enter in any
#number and the program will multiply by 10 and assign that result to the
#variable. The loop will iterate as long as product is below 100.


num = float(input("Enter a number")) #number that the user picks that will be
                                     #calculated with the product

product = num * 10 #product is the user entered number multiplied by 10

while product < 100: #while statement indicates that until the number
                     #reaches 99 but not 100 the program will continue
                     #to loop and repeate the loop
    
    print(num, " X 10 = ", product) #the num indicates the user entered
                                    #that was entered will be displayed then
                                    #the string between "" will be printed
                                    #then the , products indicates the total
                                    #of our variable product will be
                                    #displayed
    num = float(input("Product is less than 100, Please enter another number: "))
    #if the product that is calculated is less than 100 the program will
    #run again and again until the calculated number is greater than 100
    product = num * 10
    
print("The product exceeds 100 please stop!")
#if the product calculated is greater than 100 the program will stop running
#and output that your number exceeds 100.
