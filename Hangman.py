# Hangman Game
import random
from Hangman_assets import words_list, stages, logo

print(logo)

lives = 6

chosen_word = list(random.choice(words_list).strip(" "))
display = []

chosen_word_len = len(chosen_word)
# print(f"The word has {chosen_word_len} letters")

for blanks in chosen_word:
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess the letter: ").lower()
    
    if guess in display:
        print("You have already guessed the letter")
        
    for position in range(chosen_word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}.Thats not in the word.")
        lives -= 1
        if lives>1:
            print(f"You have {lives} lives left")
        if lives == 1:
            print(f"You have {lives} life left")
        if lives == 0:
            end_of_game = True
            print("Game Over")

    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You Win")                     

    print(stages[lives])
    


