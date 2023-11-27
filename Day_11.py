import random, os
from Hangman_assets import blackjack_logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has blackjack"    
    elif user_score == 0:
        return "Win with a blackjack"    
    elif user_score > 21:
        return "You went over, you lose"    
    elif computer_score > 21:
        return "Opponent went over, you win"
    elif user_score > computer_score:
        return "You win"    
    else:
        return "You lose" 
               
def play_game():
    print(blackjack_logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card()) 

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Your score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to draw another card and type 'n' to pass ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand: {user_cards}, final_score: {user_score}")
    print(f"computer's final hand: {computer_cards}, final_score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Type 'y' to play blackjack game and type 'n' to exit ") == 'y':
    os.system('cls')
    play_game()  