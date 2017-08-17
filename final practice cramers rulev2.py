#John Salazar
#8-14-17
#engr 120

def cramers_rule(a, b, c, d, e, f): #defining our main rule and has it accepting 6 arguments.

    if ((a * d) - (b * c)) == 0: #if the bottom of the eqn equals 0 then the function is returned and asks the user
                                #
        print("The equations have no solutions")
    else:

        x =( e * d - b * f) /( a * d - b * c)
        y = (a * f - e * c) / (a * d - b * c)

        user = input("Which veriable X or Y you would like to compute for? ")
        if user == 'X':
            print(x)
        else:
            print(y)

def main():
    a = int(input("Please give me a number to input into cramer's rule. "))
    b = int(input("Please give me a number to input into cramer's rule. "))
    c = int(input("Please give me a number to input into cramer's rule. "))
    d = int(input("Please give me a number to input into cramer's rule. "))
    e = int(input("Please give me a number to input into cramer's rule. "))
    f = int(input("Please give me a number to input into cramer's rule. "))

    cramers_rule(a, b, c, d, e, f)

main()