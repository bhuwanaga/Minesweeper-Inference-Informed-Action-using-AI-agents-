from GenerateBoard import *

# The game was lost because Dusty hit a mine
def game_loss(user_board, mine_board, row, col):
        print('Dusty lost the game because he hit a mine at %d,%d',(row,col))
        row = len(user_board)
        col = len(user_board[0])
        for i in range(0,row,1):
                for j in range(0,col,1):
                        if mine_board[i][j] == 9:
                                print('M')
                        else:
                                print(user_board[i][j])
                        print("")
                print('\n')

# Dusty won!!
def game_won(user_board):
        print('Dusty won the game by uncovering all cells without hitting any mines')
        printBoard(user_board)

