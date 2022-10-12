"""
File Name: wordlegame.py
Creator: Ammon Jones
Purpose: Allow a user to guess a secret word.
"""
# Libraries needed to complete the task:
import time

# Functions needed to complete the task:

# Constants needed to complete the task:
secret = 'shred'
    #secretlength = len(secret)
# Variables needed to complete the task:
guess = ''
counter = 0
guess_num = 1
# Info needed from user to complete the task:
print('Wordle-Like Game, Start Guessing Below!')
print('')
print('Understanding Hints:')
print('-An underscore _ indicates that the letter was not present in the secret word.')
print('-A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.')
print('-An uppercase letter indicates that the letter was present at that exact spot in the secret word.')
print('')
print('Your hint is: - - - - -')

while secret != guess.lower():
    print('')
    guess = input(f'Enter your guess number {guess_num}: ')
    guess_num = guess_num + 1
    while len(guess) != len(secret):
        print("Don't you know how to count??? Enter a 5 letter word!!!")
        print('Your hint is: - - - - -')
        guess = input(f'Enter your guess number {guess_num}: ')
        guess_num = guess_num + 1
    if guess.lower() != secret:
        print('Your hint is: ', end = '')
        for index in range(len(secret)):
            if secret[index] == guess[index]:
                print(secret[index].upper(), end = ' ')
            elif guess[index] in secret:
                print(guess[index].lower(), end = ' ')
            else:
                print('_', end = ' ')
guess_num = guess_num - 1  
print('')          
print(f'It took you long enough... It only took you a whole {guess_num} guesses to finally get it right!')
print(f'The word was {secret.upper()}')
time.sleep(10)




