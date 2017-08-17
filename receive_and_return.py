# This program has three functions
# One function receives a value
# One function returns a value
# One function both receives and returns a value

def display(message):
    print(message)

def give_me_five():
    five = 5
    return five

def ask_yes_no(question):
    """Ask a yes or no question and return the response"""
    response = None
    while response not in ('y', 'n'):
        response = input(question.lower())
    print ("Exiting function.")
    return response

def main():
    display("Here's a message for you.\n")

    number = give_me_five()
    print ("Here's what I got from give_me_five():", number)
    
    
    answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
    print ("Thanks for entering:", answer)

    input("We're done!")

main()
