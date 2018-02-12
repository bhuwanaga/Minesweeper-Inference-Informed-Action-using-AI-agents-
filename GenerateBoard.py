import random
import Minesweeper

class GenerateBoardUI():
	## Generate play by initializing the game with these function...
	## either in this .py or Minesweeper.py

	## This board is only available to dusty
	def gen_Mine_Board(self, rows, cols, PROBABILITY):
		rows = int(rows)
		cols = int(cols)
		mine_board = []
		prob = PROBABILITY*100
		for i in range(0,rows,1):
			mine_inner = []
			for j in range(0,cols,1):
				rand = random.randint (1, 100)
				if(rand < prob):
					mine_inner.append(1)
				else:
					mine_inner.append(0)
			mine_board.append(mine_inner)

		return mine_board

	# generate board where either a cell has 'A' for available or an integer >= 0
	def gen_user_Board(self,rows, cols):
		rows = int(rows)
		cols = int(cols)
		user_board = []
		for i in range(0,rows,1):
			user_inner = []
			for j in range(0,cols,1):
				user_inner.append('A')
			user_board.append(user_inner)
		return user_board

	# print board to terminal
	def printBoard(self,board):
		for row in board:
			for j in row:
				print(j),
			print
		print("\n")
