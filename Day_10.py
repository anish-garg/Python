# Functions with outputs 
def format_name(f_name,l_name):
    # Docstrings
    '''Takes a first and last name and format it to 
       the title case version.'''
    if f_name == "" or l_name == "":
        return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    
print(format_name(input("What is your first name? "),input("What is your last name? ")))

# Challenge 1 Days in month
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return(True)
#             else:
#                 return(False)
#         else:
#             return(True)
#     else:
#         return(False)


# def days_in_month(year,month):
#     if month > 12 or month < 1:
#         return
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) == True:
#         month_days[1] = 29
#         return month_days[month - 1]
#     else:
#         month_days[1] = 28
#         return month_days[month - 1]

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)    

# Challenge 2 Calculator
from Hangman_assets import calci_logo
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2    

def divide(n1,n2):
    return n1 / n2    
    
operators = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}

def calculator():
    print(calci_logo )
    is_calculating = True
    n1 = float(input("Write the first number:\n"))
    while is_calculating:
        n2 = float(input("Write the second number:\n"))
        for key in operators:
            print(key)
        operation = input("Pick an operation:\n")    

        # if operation == "+":
        #     answer = add(n1,n2)
        # elif operation == "-":
        #     answer = sub(n1,n2)
        # elif operation == "*":
        #     answer = multiply(n1,n2)
        # elif operation == "/":
        #     answer = divide(n1,n2)
        # else:
        #     print("Invalid input")    

        calculation_function = operators[operation]    
        answer = calculation_function(n1,n2)
        print(f"{n1} {operation} {n2} = {answer}")
        
        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:  ")
        if cont == 'y':
            n1 = answer
        elif cont == "n":
            is_calculating = False
            calculator()
        else:
            print("Wrong input") 

calculator()               

      
