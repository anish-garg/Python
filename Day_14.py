# Higher Lower game
import random, os
from Higher_lower import data, vs, logo

current_score = 0
is_game_over = False

def check_answer(guess,A,B):
    global is_game_over
    if guess == 'A':
        if A["follower_count"] > B["follower_count"]:
            return current_score + 1
        else:
            is_game_over = True
            return current_score
    elif guess == 'B':
        if A["follower_count"] < B["follower_count"]:
            return current_score + 1
        else:
            is_game_over = True
            return current_score
    else:
        print("Wrong Input")
 
print(logo)
while not is_game_over:
    A = random.choice(data)
    B = random.choice(data)
    
    print(f"Compare A: {A["name"]}, {A["description"]}, from {A["country"]} ")
    print(vs)
    print(f"Against B: {B["name"]}, {B["description"]}, from {B["country"]} ")

    guess = input("Who has more followers? Type 'A' or 'B'. ")

    current_score = check_answer(guess,A,B)
    os.system('cls')
    print(logo)
    if is_game_over == False:
        print(f"You are right. Current score: {current_score}")
    else:
        print(f"Sorry you lose. Final score: {current_score}")