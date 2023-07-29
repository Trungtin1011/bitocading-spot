import random

min, max = 1, 10
rand_num: int = random.randint(min, max)

while True:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number!')
        continue
    
    if user_guess > rand_num:
        print('The number is lower')
    elif user_guess < rand_num:
        print('The number is higher')
    else:
        print('You guessed it!')
        break