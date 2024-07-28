board: list = [" " for i in range(9)]

def print_board():
    print(f"\t|{board[0]}|{board[1]}|{board[2]}|")
    print(f"\t|{board[3]}|{board[4]}|{board[5]}|")
    print(f"\t|{board[6]}|{board[7]}|{board[8]}|")

def move(player):
    while True:
        if player == "X":
            player_id: int = 1
        if player == "O":
            player_id: int = 2

        print("============================")
        print(f"--- Player {player_id}:")

        try:
            choice: int = int(input("Please select your move (1-9) >> ").strip())
            if choice < 1 or choice > 9:
                raise ValueError
            if board[choice - 1] == " ":
                board[choice-1] = player
            else:
                print()
                print('The space is taken')
            break
            
        except ValueError as e:
            print("Please choose valid move!")
            continue

def is_win(player):
    if (board[0] == player and board[1] == player and board[2] == player ) or \
       (board[3] == player and board[4] == player and board[5] == player ) or \
       (board[6] == player and board[7] == player and board[8] == player ) or \
       (board[0] == player and board[3] == player and board[6] == player ) or \
       (board[1] == player and board[4] == player and board[7] == player ) or \
       (board[2] == player and board[5] == player and board[8] == player ) or \
       (board[0] == player and board[4] == player and board[8] == player ) or \
       (board[2] == player and board[4] == player and board[6] == player ):
        return True
    else:
        return False

def play():
    print("=== Welcome to Caro 3x3 ===")
    print("============================")

    while " " in board:
        print_board()
        move('X')
        print_board()
        if is_win('X'):
            print("Player X wins!")
            break
        move('O')
        if is_win('O'):
            print_board()
            print("Player O wins!")
            break

    if " " not in board:
        print()
        print("Out of moves, Game Over!!!")

play()