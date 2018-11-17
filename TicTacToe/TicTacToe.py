import os

# display board
def show_board(board):
    # structure to create board
    pat_list = \
    [ list('   |   |   ')\
    , list('-----------')\
    , list('   |   |   ')\
    , list('-----------')\
    , list('   |   |   ')]

    # first row
    pat_list[0][1] = board[0]
    pat_list[0][5] = board[1]
    pat_list[0][9] = board[2]
    # second row
    pat_list[2][1] = board[3]
    pat_list[2][5] = board[4]
    pat_list[2][9] = board[5]
    # third row
    pat_list[4][1] = board[6]
    pat_list[4][5] = board[7]
    pat_list[4][9] = board[8]

    for i in range(5):
        print(''.join(pat_list[i]))

# Function to make the marker swith permenent
def select_marker(marker):    
    marker = marker.upper()
    if (marker == 'X'):
        return (('X', '0'))
    else:
        return (('0', 'X'))


# Function to check the win condition
def check_victory(board):

    if ((board[0] == board[1] == board[2] == 'X') or (board[0] == board[1] == board[2] == '0')\
    or (board[0] == board[3] == board[6] == 'X') or (board[0] == board[3] == board[6] == '0')\
    or (board[0] == board[4] == board[8] == 'X') or (board[0] == board[4] == board[8] == '0')\
    or (board[3] == board[4] == board[5] == 'X') or (board[3] == board[4] == board[5] == '0')\
    or (board[1] == board[4] == board[7] == 'X') or (board[1] == board[4] == board[7] == '0')\
    or (board[2] == board[5] == board[8] == 'X') or (board[2] == board[5] == board[8] == '0')\
    or (board[6] == board[7] == board[8]== 'X') or (board[6] == board[7] == board[8]== '0')\
    or (board[2] == board[4] == board[6]== 'X') or (board[2] == board[4] == board[6]== '0')):
        return True
    else:
        return False


# Function to clear the screen
def clear_screen():
    os.system('cls')


# Main function, where the magic begins.
def main():
    os.system('cls')

    print("Welcome to TicTacToe")
    print("Players be ready!!!\n")

    marker = select_marker(str(input\
    ("Player 1, Please select your marker (X or 0): ")))

    print("Let's start!!!")

    i = 0
    victory_status = False
    continue_status = True
    chance = ''
    initial_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    #current_board = initial_board

    show_board(initial_board)
    while continue_status == True:
        current_board = initial_board
        while victory_status == False:
            # player 1 logic
            chance = 'Player 1'
            pos_playerOne = (int(input\
            ("Player 1, please place your marker on the borad (1 - 9): "))) - 1;

            if (i < 1):
                current_board[pos_playerOne] = marker[0]
            else:
                if (current_board[pos_playerOne] == 'X' \
                or current_board[pos_playerOne] == '0'):
                    int(input("%*% %*% %*%%*% %*% %*%\n\
                    The slected postion is already filled.\
                    \n%*% %*% %*%%*% %*% %*%\n\
                    Please select correct position: "))
                else:
                    current_board[pos_playerOne] = marker[0]
            i += 1
            # Clear screen and print current board
            clear_screen()
            show_board(current_board)
            victory_status = check_victory(current_board)

            # check if the 9 board inputs are completed, total
            # 9 columns are available for playes to select.
            if (i >= 9):
                print('\n\n!!! Game Over !!!\n\n')
                break
            if victory_status == True:
                break
            ###############################################################
            ###############################################################
            ###############################################################
            # player 2 logic
            chance = 'Player 2'
            pos_playerTwo = (int(input\
            ("Player 2, please place your marker on the borad (1 - 9): "))) - 1
            
            if (current_board[pos_playerTwo] == 'X' \
            or current_board[pos_playerTwo] == '0'):
                int(input("%*% %*% %*%%*% %*% %*%\n\
                The slected postion is already filled.\
                \n%*% %*% %*%%*% %*% %*%\n\
                Please select correct position: "))
            else:
                current_board[pos_playerTwo] = marker[1]
            # Clear screen and print curent board
            i += 1
            clear_screen()
            show_board(current_board)
            victory_status = check_victory(current_board)
            if victory_status == True:
                break

        if victory_status == True:
            print("Congratulations {}!!! You have won!!! \n".format(chance))
        elif i == 9:
            print("Game tied.\n")
        else:
            print("Exception\n")

        continue_status = input("Would you like to continue? (Y or N)")
        if continue_status == 'Y' or continue_status == 'Yes':
            continue_status = True
        else:
            continue_status = False


if __name__ == '__main__':
    main()