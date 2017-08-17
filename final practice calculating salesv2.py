#John Salazar
#8-14-17
#engr 120

def calSales(No, amount): #accepts 2 variables for number or products sold as well as amount of the product

    #depending on product number selected these product prices will be used multiplied by the amount sold. put into
    #the def for calSales.

    if No == 1:
        price = 2.98
    elif No == 2:
        price = 4.50
    elif No == 3:
        price = 9.98
    elif No == 4:
        price = 4.49
    else:
        price = 6.87

    sales = price * amount    #price * amount is put into the variable sales so that we can return the calculated
                              #sales depending on the choices made.

    return sales      #the calculated price * amount is returned to the main function of calSales()


num_of_prod = int(input("How many of the product were sold? ")) #ask the user to give us the product he would like
prod_sold = int(input("which product was sold? "))


print(calSales(prod_sold, num_of_prod))