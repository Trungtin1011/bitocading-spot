import random
def run_game():
    word: str = random.choice(['apple', 'secret', 'banana'])

    uname: str = input('What is your name? >> ')
    print(f'Welcome to hangman, {uname}!')

run_game()