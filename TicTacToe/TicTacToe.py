import os

def test_board(board):
    pat_list = [list('   |   |   '), list('-----------'), list('   |   |   '), list('-----------'), list('   |   |   ')]
    #board = ['0', 'X', '0','0', 'X', '0','0', 'X', '0']

   
    pat_list[0][1] = board[0]
    pat_list[0][5] = board[1]
    pat_list[0][9] = board[2]

    pat_list[2][1] = board[3]
    pat_list[2][5] = board[4]
    pat_list[2][9] = board[5]

    pat_list[4][1] = board[6]
    pat_list[4][5] = board[7]
    pat_list[4][9] = board[8]

    for i in range(5):
        print(''.join(pat_list[i]))

def select_marker(marker):    
    marker = marker.upper()
    if (marker == 'X'):
        return (['X', '0'])
    else:
        return (['0', 'X'])

def main():
    os.system('cls')

    print("Welcome to TicTacToe")
    print("Players be ready!!!\n")

    marker = select_marker(str(input("Player 1, Please select your marker (X or 0): ")))

    print("Let's start!!!")

    i = 0
    initial_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_board = initial_board

    test_board(initial_board)

    while True:
        pos_playerOne = (int(input("Player 1, please place your marker on the borad (1 - 9): "))) - 1;

        if (i < 1):
            current_board[pos_playerOne] = marker[0]
        else:
            if (current_board[ pos_playerOne] == 'X' or current_board[pos_playerOne] == '0'):
                print("%*% %*% %*%\nThe slected postion is already filled. \n%*% %*% %*%\nPlease select correct position: ")
            else:
                current_board[pos_playerOne] = marker[0]
        i += 1
        print(current_board)
        if (i > 9):
            break  


if __name__ == '__main__':
    main()