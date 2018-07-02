
# Try using Jupyter Notebook to test each and every function saperatly.
# For using the same code in either Python 2 or 3
from __future__ import print_function

## Note: Python 2 users, use raw_input() to get player input. Python 3 users, use input()


'''
Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
'''
from IPython.display import clear_output
def display_board(board):

    clear_output()

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('-----------')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('-----------')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])



'''
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
'''
def player_input():

    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

'''
Step 3: Write a function that takes, in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
'''
def place_marker(board, marker, position):
    board[position] = marker


'''
Step 4: Write a function that takes in a board and checks to see if someone has won. Indicate all winning combinations
'''
def win_check(board,mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal



'''
Step 5: Write a function that uses the random module to randomly decide which player goes first.
'''
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


'''
Step 6: Write a function that returns a boolean (True or False) indicating whether a space on the board is freely available.
'''
def space_check(board, position):

    return board[position] == ' '


'''
Step 7: Write a function that checks if the board is full and returns a boolean value (True or False). True if full, False otherwise.
'''
def full_board_check(board):
    for i in range(1,10):               # for loop is to iterate through all the apaces on the board and verify if the board is empty or not.
        if space_check(board, i):
            return False
    return True


'''
Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. If it is, then return the position for later use.
'''
def player_choice(board):
    # Using strings because of input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):  # You can either use sting like '1 2 3 4 5 6 7 8' or a list ['1', '2', '3', '4', '5', '6', '7', '8', '9']. Both will give the same result.

        position = input('Please Choose from (1-9)')
    return int(position)


'''
Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
'''
def replay():

    return input('Do you want to play again? Enter Yes (Y) or No (N): ').lower().startswith('y')


'''
first make sure the board is clean before you start the game. Then ask for player input by using the function we ahve created till now.
'''

print('Welcome to Tic Tac Toe!')

while True:
    # Reset` the board
    theBoard = [' '] * 10       # to make sure we are using empty board to start the game
    player1_marker, player2_marker = player_input()   # To choose the player markers for each player using player_input function
    turn = choose_first()       # Call the choose_first funtion to randomly select the player to start the game
    print(turn + ' will go first.')   # Print the randomly selected player information. So that the selected player will start the game.

    play_game = input('Ready to play? y or n?')  # ask for player confirmation if he wants to start the game or not.

    if play_game.lower() == 'y':    # If player wants to start the game or not, assign that boolean value to new variable
        game_on = True
    else :
        game_on = False

    while game_on:   # if player wants to start the game (if the value of game_on is TRUE) then we enter into the loop
        if turn == 'Player 1':
            # Player1's turn.
            print("Player 1: Enter your Choice: ")
            display_board(theBoard)             # Display the board to player with all the marked slots filled or an empty board if its the first selection
            position = player_choice(theBoard)   # Choose the marker for the player

            place_marker(theBoard, player1_marker, position)  #Place the choosen marker at the appropriate position

            if win_check(theBoard, player1_marker):     #Check the condition if the player won or not
                display_board(theBoard)
                print('Congratulations Player1..! You have won the game..!')    #if the player has one print the message indicating the player has won else enter into the loop againa nd ask the player to choose the marker
                game_on = False
            else:
                if full_board_check(theBoard):          # Verify the condition where no player has won
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            print("Player 2: Enter your Choice: ")
            display_board(theBoard)
            position = player_choice(theBoard)

            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations Player2..! You have won the game..!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
