# Loops

fruits =["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

# Challenge 1 Average height
# student_heights = input("Enter a list of heights ").split()
# for n in range(0,len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)   

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f"Total height is {total_height}")

# total_students = 0
# for student in student_heights:
#     total_students += 1
# print(f"Total no of students are {total_students}")    

# -----------------------------------------------------------------------------------------

# avg_height = round(total_height / total_students, 2)
# print(f"Average height is {avg_height}")
    
# Challenge 2 Highest score
# student_scores = input("Enter the list of scores ").split()
# for n in range(0,len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)    

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#       max_score = score
# print(f"The highest score in the class is: {max_score}")      

# -----------------------------------------------------------------------------------------

# range in loops
# for number in range(start_point,end_point,step_skip)
for number in range(1,11,3):
    print(number)

total = 0
for number in range(1,101):
    total += number
print(total)

# Challenge 3 Adding evens
# sum = 0
# for number in range(0,101,2):
#     sum += number
# print(sum)    

# Challenge 4 FizzBuzz
# for number in range(1,101):
#     if(number % 3 == 0 and number % 5 == 0):
#         print("FizzBuzz")
#     elif(number % 3 == 0):
#         print("Fizz")    
#     elif(number % 5 == 0):
#         print("Buzz")    
#     else:
#         print(number)   





    