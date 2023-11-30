# Scopes in Python

# Any variable inside if, else, for, or while loop is a global variable.
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level == 3:
    new_enemy = enemies[1]

print(new_enemy)    

# Any variable inside a function is a local variable
def createPlay():
    villains = ["Skeleton", "Aliens", "Zombie"]
    if game_level == 3:
        new_villain = villains[0]
       
    print(new_villain)  
createPlay()          

# Modifying global scope
enemy = 1
def increaseEnemy():
    # To use a global variable inside a function we need to use global keyword or you can use return statement in function
    # global enemy
    # enemy += 1

    return enemy + 1 
print(increaseEnemy())    

# Challenge 1 Number guessing game
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
#   print(f"The correct answer is {answer}") 

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

