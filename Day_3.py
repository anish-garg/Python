# If and else statements 
# Logical operators
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm "))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age "))
    if age < 12:
        bill = 50
        print(f"You have to pay {bill} rupees")
    elif age<=18:
        bill = 100
        print(f"You have to pay {bill} rupees")
    elif age >=  45 and age <= 55:    
        print("No need to worry. You have a free ride on us")
    else:
        bill = 150
        print(f"You have to pay {bill} rupees")  
    want_photos = input("Do you want a photo? Y or N. ")   
    if want_photos == "Y":
        bill += 10
        print(f"Your total bill is {bill} rupees")
    if want_photos == "N":
        bill = bill
        print(f"Your total bill is {bill} rupees")    
else:
    print("You need to grow taller to ride the rollercoaster")      

# ----------------------------------------------------------------------------------- # 

# Challenge 1
# number = int(input("Which number you want to check "))
# if number % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd number")    

# ----------------------------------------------------------------------------------- # 

# Challenge 2 BMI calculator 2.0
# height = float(input("Enter your height in m "))
# weight = float(input("Enter your weight in kgs "))

# bmi = round(weight / height ** 2,1)
# if bmi<18.5:
#     print("You are underweight")
# elif bmi<25:
#     print("You are normal weight")
# elif bmi<30:
#     print("You are overweight")
# elif bmi<35:
#     print("You are obese")
# else:
#     print("You are clinically obese")                

# ----------------------------------------------------------------------------------- # 

# Challenge 3 Leap year checker
# year = int(input("Which year do you want to check? "))

# if year % 4 != 0:
#     print(f"{year} is not a leap year")
# else:
#     if year % 100 != 0:
#             print(f"{year} is a leap year")
#     else:
#         if year % 400 == 0:
#             print(f"{year} is  a leap year")
#         else:
#             print(f"{year} is not a leap year")

# ----------------------------------------------------------------------------------- # 

# Challenge 4 Pizza Order
# print("Welcome to pizza deliveries!")
# size_choice = input("What size of pizza would you like (s/m/l)? ")
# add_onion = input("Do you want onion in your pizza  Y or N ? ")
# extra_cheese = input("Do you want extra cheese in your pizza  Y or N ? ")
# bill = 0

# if size_choice == "s":
#     bill += 70     
# elif size_choice == "m":
#     bill += 90
# else:
#     bill += 110
    
# if add_onion == "Y":
#     if size_choice == "s":
#         bill += 20
#     else:
#         bill += 30
   
# if extra_cheese == "Y":
#     bill += 10
    
# print(f"Your total bill is {bill} rupees")    

# ----------------------------------------------------------------------------------- # 

# Challenge 5 Love calculator
# print("Welcome to love calculator")
# name_1 = input("What is your name?\n")
# name_2 = input("What is your partner's name?\n")

# name = name_1 + name_2
# new_name = name.lower()

# t = new_name.count("t")
# r = new_name.count("r")
# u = new_name.count("u")
# e = new_name.count("e")

# true = t + r + u + e

# l = new_name.count("l")
# o = new_name.count("o")
# v = new_name.count("v")
# e = new_name.count("e")

# love = l + o + v + e

# love_score = int(str(true) + str(love))

# if love_score < 10 or love_score > 90:
#     print(f"Your love score is {love_score}%. You go together like coke and mentos.")
# elif love_score >= 40 and love_score <= 50:
#     print(f"Your love score is {love_score}%. You are alright together")    
# else:
#     print(f"Your love score is {love_score}%.")

# ----------------------------------------------------------------------------------- # 

# Challenge 6 Treasure Island
print("Welcome to treasure island!")
first = input("Where do you want to go left or right?\n")

if first == "left":
   second = input("You have come to lake. What do you want to do swim or wait?\n")
   if second == "swim":
    third = input("You have arrived at the island. There are 3 doors so, which door you want to choose red, blue or yellow?\n")
    if third == "yellow":
        print("You won the treasure")
    elif third == "red":
        print("You entered a room full of fire.Game Over")
    elif third == "blue":
        print("You entered a room full of beasts.Game Over")    
    else:
        print("Game Over")
   else:
    print("Hunters caught you because you were waiting.Game Over") 
else:
    print("Game Over")                   