#John Salazar
#08-11-17
#quiz 7


def main():
    num = int(input("Please enter a number and I will tell you if it is Even or Odd: "))
    isEven(num)


def isEven(mod):
    if mod % 2 == 0:
        print("Your number is Even")
    else:
        print("Your number is Odd")

main()