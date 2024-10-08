import os
import random
from words import word_list
from hangman_visual import lives_visual_dict
import webbrowser

url = "https://youtu.be/13V0RcKImLU?si=8ldHWBqf7oFUfCOO"

def randomword():
    word = random.choice(word_list)
    return word

def char_input(string):
    while True:
        try:
            word = input(string)
            word_index = list(word)
            if len(word_index) == 1:
                return word
        except ValueError:
            print('Valor invalido digite novamente')


def game():
    word = randomword()
    word_find = list(word)
    found = []
    lives = 0
    print('Bem vindo a forca')
    for num in range(len(word_find)):
        found.append('*')
    while True:
        choice = char_input('Digite a letra desejada: ').lower()
        if choice in word_find:
            for index,char in enumerate(word_find):
                if char == choice:
                    found[index] = choice
        else:
            lives += 1
            if lives > 7:
                print('Você perdeu burrão')
                webbrowser.open_new(url)
                input('Digite enter para sair')
                break
            else:
                print('Errou')

        print(lives_visual_dict[lives])
        print(found)

        if found == word_find:
            print(f'Você ganhou a palavra era {word}')
            input('Digite enter para sair')
            break
        if lives == 7:
            print('Você perdeu burrão')
            webbrowser.open_new(url)
            input('Digite enter para sair')
            break

def main():
    game()

main()