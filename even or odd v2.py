#John Salazar
#08-11-17
#quiz 7



def main():
    number = int(input("Please enter a number and I will tell you if it is Even or Odd: "))
    isEven(number)

def isEven(num):

    if num % 2 == 0:
        print("Your number is Even")
    else:
        print("Your number is Odd")

main()