#######################################
### Dice game
#######################################

import random

### Use Type Hint: "-> list[int]"
def roll(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    ### Variable annotation: "rolls: list[int]"
    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll? ')

            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break
            
            print (*roll(int(user_input)), sep=', ')

        except ValueError as e:
            print('(Please input a valid number!)')
            continue

main()