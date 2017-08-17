#John Salazar
#8-14-17
#engr 120

def main():
    num_employees = get_number() #setting variable in main = to our variable in our function get_number that was
                                #returned.

    num_days = total_days(num_employees)  #setting variable in main = to our 2nd nested function so that when we call
                                          # the main function our variable num_days will pick up the returned value
                                          #from our function total_days(employees)

    ave = average(num_employees, num_days)  #the variable ave we set = to our function and again use out 2
                                            # arguments we have set to our new variable, num_employees and num_days

    print("The average days missed by your employees is", ave ) # finally we print out our calculations that the
                                                                #variable ave will compute.

def get_number():
    employees = int(input("How many employees does the company have?  ")) #ask for user input for the number of
                                                                    #employees the company has.

    while employees < 1: # set a while loop for anything under 1 this will happen

        print("You can't have less than 1 employees, Please re-enter") #if input is less than 1 it will print a new
                                                                #request for you to enter another number greater than 0

        employees = int(input("How many employees does the company have?  ")) #input will again ask you to input
                                                                #another number that is greater than 0

    return employees #after you have entered in a number that is 1 or greater the return employees function will
                     #will return the user inputted value to main so that it can be stored in a variable.

def total_days(employees): # accepts 1 argument and that is the number of employees

    days_missed = int(input("How many days have your employees missed?  ")) #asks you to input the number of days
                                                    #missed for all employees

    while days_missed < 0: # asks you to input a number from 0 to positive infinity

        print("Please enter a number greater than or equal to 0") #if you enter a number that is lower than 0 it will
                                                    #ask you to re-input a number that is greater than 0

        days_missed = int(input("How many days have your employees missed?  ")) #asks the user to input how many days
                                                    #the employees have missed

    return days_missed #returns the user input for the amount of days missed by the employees to main so that
                      #the figure can be again stored in a variable and used for calculations.

def average(employees, days_missed): #accepts 2 arguments for the number of employees and the number of days missed.

    avg_num_day_miss = days_missed / employees #  sets a variable = to days missed divided by employees

    return avg_num_day_miss #returns the variable with the calculation for avg number of days missed.

main() #call the main() function so that the set variables can run the function and calculate the totals.