from GenerateBoard import GenerateBoardUI
from Minesweeper import Minesweep
from GameState import *

def main ():
	mine_board = [[2,9,1,0,1,9], [9,3,1,0,1,1],[9,2,0,0,0,0],[2,2,1,0,1,1],[1,9,2,2,2,9],[1,2,9,2,9,1,]]
	maze = GenerateBoardUI()
	sweep = Minesweep()
	print('Board filled with mines')
	maze.printBoard(mine_board)
	user_board = maze.gen_user_Board(6, 6)
	sweep.gen_open_cells(user_board, mine_board)
	maze.printBoard(user_board)



if __name__ == '__main__':
	main ()