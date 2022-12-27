# Day 10 - Calculator 
from art import logo

#Addition 
def add(n1,n2):
    return n1+n2

#Subtraction
def subtract(n1,n2):
    return n1-n2

#Multiplication
def multiply(n1,n2):
    return n1 * n2

#Division
def divide(n1,n2):
    return n1/n2

#dictionary for all the operations 
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

#Recursive function
def calculator():
    print(logo)
    num1= float(input("What's the first number? : "))
    for key in operations:
        print(key)

    #Flag
    should_continue = True

    while should_continue:
        op = input("Pick an operation : ")
        num2= float(input("What's the next number? : "))

        #assign the values in calculation_function
        calculation_function = operations[op]
        #passing num1 and num2 values in calculation_function
        #saving the value in another var = answer
        answer = calculation_function(num1,num2)

        print(f"{num1} {op} {num2} = {answer}") 

        choice = input(f"What would you like to do?\nType '1' if you want to continue calculating with {answer}\nType '2' to start a new calculation\nType '3' to exit : ")
        if choice == "1":
            num1 = answer
        elif choice == "3":
            should_continue = False 
            print("Thank you")
        else:
            #recursively calling the function calculator 
            calculator()

calculator()