import random
import hangman_stages
import word_file

lives = 6
chosen_word = random.choice(word_file.words)

num_hints = 3
hint_indices = random.sample(range(len(chosen_word)), num_hints)

display = []
for i in range(len(chosen_word)):
    if i in hint_indices:
        display.append(chosen_word[i])
    else:
        display.append("_")

print("Welcome to the game of Hangman!!")
print(display)  # Initial display with hints

game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -=1
        if lives==0:
            game_over = True
        print("You lose!!!")
        
    if '_' not in display:
        game_over = True
        print("You win!!!")
    print(hangman_stages.stages[lives])# ... (rest of your game logic)
