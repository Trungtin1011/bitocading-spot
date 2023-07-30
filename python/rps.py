#######################################
### Rock - Paper - Scissor game
#######################################

import random
import sys

class RPS:
    ### All classes have a function called __init__()
    def __init__(self):
        print('Welcome to Rock-Paper-Scissor game!')

        self.moves: dict = {'rock': '🪨', 'paper': '📜', 'scissor': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play(self):
        print('')
        user_choice: str = input('Rock, paper, or scissor? >> ').lower()

        if user_choice == 'exit':
            print('Thanks for playing!')
            sys.exit()
        
        if user_choice not in self.valid_moves:
            print('Invalid choice...')
            return self.play() 
        
        ai_choice: str = random.choice(self.valid_moves)

        self.display(user_choice, ai_choice)
        self.check_move(user_choice, ai_choice)

    def display(self, user_choice: str, ai_choice: str):
        print('---')
        print(f'You: {self.moves[user_choice]}')
        print(f'AI: {self.moves[ai_choice]}')
        print('---')
    
    def check_move(self, user_choice: str, ai_choice: str):
        if user_choice == ai_choice:
            print('It\'s a tie!')
        elif user_choice == 'rock' and ai_choice == 'scissor':
            print('You win!')
        elif user_choice == 'scissor' and ai_choice == 'paper':
            print('You win!')
        elif user_choice == 'paper' and ai_choice == 'rock':
            print('You win!')
        else:
            print('AI wins...')


rps = RPS()

while True:
    rps.play()