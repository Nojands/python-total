# Here we are going to build the Hangman game

import random
from random import *

words_list = ['dinosaurio', 'caricatura', 'primavera', 'herramientas', 'cenicienta', 'instrucciones', 'boligrafo', 'mensualidad', 'mariposas', 'aventuras']
lives = 6
tries = 0
user_list_letters = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
good_letters = []
bad_letters = []

end_game = False
unique_letters = 0

def chose_word(list_of_words):
    global unique_letters
    word_chosen = choice(list_of_words)
    unique_letters = len(set(word_chosen))

    return word_chosen

def ask_letter():
    chosen_letter = ''
    valid = False

    while not valid:
        chosen_letter = input('Elige una letra: ').lower()
        if chosen_letter in alphabet and len(chosen_letter) == 1:
            valid = True
        else:
            print("No elegiste una letra correcta")

    return chosen_letter

def show_updated_hyphens(word_chosen):
    hidden_list = []
    for letter in word_chosen:
        if letter in good_letters:
            hidden_list.append(letter)
        else:
            hidden_list.append('-')
    print(' '.join(hidden_list))

def review_letter(chosen_letter, hidden_word, lives, coincidences, unique_letters):
    end = False

    if chosen_letter in hidden_word:
        good_letters.append(chosen_letter)
        coincidences += 1
    else:
        bad_letters.append(chosen_letter)
        lives -= 1

    if lives == 0:
        end = lose_game()
    elif coincidences == unique_letters:
        end = win_game(hidden_word)

    return lives, end, coincidences

def lose_game():
    print('Lo siento, has perdido, te has quedado sin vidas')
    print("La palabra correcta era " + word)

    return True

def win_game(unhidden_word):
    show_updated_hyphens(unhidden_word)
    print("¡Felicidades, has GANADO!")

    return True

word = chose_word(words_list)

while not end_game:
    print('\n' + '*' * 20 + '\n')
    show_updated_hyphens(word)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(bad_letters))
    print(f"Vidas: {lives}")
    print('\n' + '*' * 20 + '\n')
    letter = ask_letter()

    lives, finished, tries = review_letter(letter, word, lives, tries, unique_letters)

    end_game = finished
