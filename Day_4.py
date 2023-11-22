import random
# import Day_1

random_no = random.randint(1,10)
print(random_no)

random_float = random.random() * 10
print(random_float)

# Challenge 1 Coin flipper
# random_side = random.randint(0,1)
# if random_side == 0:
#     print("Heads")
# else:
#     print("Tails")    

states_of_india = ["Haryana","Delhi","Maharashtra","Goa","Gujarat"]
print(states_of_india[1])    
# - in front of index will start the list from the end
print(states_of_india[-1])

states_of_india[2] = "Assam"
print(states_of_india[2])

# append will add the word at the end of the list
states_of_india.append("Himachal Pradesh")

# Challenge 2 
# names = input("Give me everybody's name separated by comma ") 
# names_list = names.split(", ")
# no_of_people = len(names_list)

# name_choose = random.randint(0,no_of_people - 1)
# print(names_list[name_choose] + " is going to buy meal for everyone")

# name_choose = random.choice(names_list)
# print(name_choose + " is going to buy meal for everyone")

# Challenge 3
# row_1 = ["⬜","⬜","⬜"]
# row_2 = ["⬜","⬜","⬜"]
# row_3 = ["⬜","⬜","⬜"]
# board = [row_1,row_2,row_3]
# print(f"{row_1}\n{row_2}\n{row_3}\n")

# position = input("Where do you want to place the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])
# board[vertical - 1][horizontal - 1] = "X"

# print(f"{row_1}\n{row_2}\n{row_3}")

# Challenge 4 Rock,paper and scissors game 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

outcomes = [rock,paper,scissors]

player = int(input("what do you choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))
if player >= 3 or player < 0:
  print("Invalid number")
else:   
  print(outcomes[player])
  computer = random.randint(0,2)
  print(f"Computer chose:\n {outcomes[computer]} ")

  if computer == 2 and player == 0:
    print("You win!")
  elif computer == 0 and player == 2:
    print("You lose")         
  elif computer > player:
    print("You lose")
  elif player > computer:
    print("You win")    
  elif computer == player:
    print("Its a draw")
  

        