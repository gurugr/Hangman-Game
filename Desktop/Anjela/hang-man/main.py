import random
from hangman_ascii import HANGMANPICS

word_list = ["book","peen","stuudent","compputer"]
rand_word = random.choice(word_list)
user_gues_word = ['_' for char in rand_word]
score = 0

print(user_gues_word)
guess_again = True
while guess_again:
    if score > 5:
        print("You lose a life...😭")
        guess_again = False
    else:
        if '_' in user_gues_word:
            guess = input("Guess the word ")
            if guess in rand_word:
                for position in range(len(rand_word)):
                    index_letter = rand_word[position]
                    if index_letter == guess:
                        user_gues_word[position] = index_letter

                print(user_gues_word)

            else:
                print(f"{guess} is not in the list. try to guess again;")
                score += 1
                print(HANGMANPICS[score])
        else:
            print("You save a life")
            guess_again = False




