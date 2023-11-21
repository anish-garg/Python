#Data types

#String
# print("Hello"[0])

#Integer
# print(123 + 456)

#Float
# print(314.71)

#Boolean
# True
# False 

num_char = len(input("What is your name? "))

new_num_char = str(num_char)

# Cannot concatenate different data types so we have to convert it to the same data type
print("Your name has " + new_num_char + " characters")

print(70 + float("100.5"))

print(str(70) + str(100))

# Challenge 1
# two_digit_num = input("Write your number ")

# num_1 = int(two_digit_num[0])
# num_2 = int(two_digit_num[1])

# sum = num_1 + num_2 
# print("Sum is " + str(sum))

# Mathematical operations
print(3 + 5)
print(10 - 5)
print(3*5)
print(6/3)
print(2**3)

# Python follows PEMDASLR rule for the mathematical operations
# Parentheses, Exponents, Multiplication and Division, Addition and Subtraction, left-to-right
print(3+3*5/5-1)

# Challenge 2 BMI calculator
# weight =  input("Enter your weight in kgs ")
# height = input("Enter your height in m ")

# new_weight = int(weight)
# new_height = float(height)

# bmi = new_weight/new_height**2

# print(int(bmi))

# Number Manipulation
print(round(8/3,3))
# // converts the float data type to int type during division
print(8//3)

result = 2
result += 1
print(result)

# f-string
score = 0 
height = 1.8
isWinning = True

print(f"Your score is {score} , Your height is {height} , {isWinning}")


# Challenge 3 Tip calculator
amount = input("Enter the amount of your bill ")
total_amount = int(amount)
tip = input("How much percentage tip would you like to give? ")
new_tip = float(tip)
final_cost = total_amount + total_amount * (new_tip/100)
people = input("Enter the number of people for the bill split ")
new_people = int(people)
share = "{:.2f}".format(final_cost/new_people)
print(f"Everyone's share will be {share} rupees")