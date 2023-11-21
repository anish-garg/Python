# print("Day 1- Python Print Function")
# print("The function is declared like this")
# print("print('what to print')")

# By '\n' we can add enter into the line without typing other print statements
# print("Hello World\nHello World\nHello World")

# String Manipulation
# By '+' we can concatenate the strings
print("Hello" + " World")

# Input function allows the user to put the info in the terminal
input("What is your name? ") 
print("Hello " + input("What is your name? ")) 

# len is used to get the length of the string
print(len(input("What is your name? ")))

# Python Variables
name = input("What is your name? ")
length = len(name)
print(name)
print(length)

a = input("a: ")     
b = input("b: ")     
c = a
a = b
b = c

print("a:",a)
print("b:",b)

# Band Project
print("Welcome to the band name generator.")
city_name = input("Whats the name of the city you grew up in?\n")
pet_name = input("Whats the name of your pet?\n")
band_name = city_name + " " + pet_name
print(band_name) 
