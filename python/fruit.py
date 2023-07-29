
#######################################
### Guess fruit name char by char
#######################################

import random
def run_game():
    word: str = random.choice(['apple', 'orange', 'banana', 'kumquat'])

    ### Input user's name
    uname: str = input('What is your name? >> ')
    print(f'Welcome to hangman, {uname}!')

    guessed: str = ''
    
    ### Maximum of 3 tries
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print() #Add a blank line

        if blanks == 0:
            print('You got it!')
            break
        
        guess: str = input('Enter a letter: ')

        if guess in guessed:
            print(f'You already used: "{guess}". Please try with another letter!')
            continue
        
        guessed += guess
        
        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong...({tries} tries remaining)')

            if tries == 0:
                print('No more tries remaining ... You lose.')
                break
                  


run_game()