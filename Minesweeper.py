from GameState import *
import random

class Minesweep():

	## gen_open_cells - function randomly opens a cell to start the game
	##
	## paremters - 
	##		user_board - board of 'A', avaiable, or integers >= 0
	##		mine_board - an integer >=0 and <= 8 is number of mines surronding,
	##						 a cell with a 9 indicates a mine, game over
	##
	## 1) game ends if cell querried is a 9
	## 2) neighbors are queeried if cell is 0 (no mines in neighbors)
	## 3) choose random neighbor if cell returns a 1
	## 4) choose random anywhere in board if cell returns 2
	def gen_open_cells(self,user_board, mine_board):
		zero = []
		myset = []

		while(True):
			# x = random.randint(0, len(user_board)-1)
			# y = random.randint(0,len(user_board[0])-1)
			x = 3
			y = 3
			if mine_board[x][y] == 9:
				game_loss(user_board, mine_board, x, y)
				break
			elif mine_board[x][y] == 0:
				user_board[x][y] = mine_board[x][y]
				zero.append([x,y])
				myset.append([x,y])
				self.recursively_traverse_neighbors(user_board, mine_board, myset, zero)
				break
			elif mine_board[x][y] == 1:
				if(isEdge(user_board, mine_board, row, col) == False and isCorner(user_board, mine_board, row, col) == False):
					user_board[x][y] = mine_board[x][y]
					self.random_neighbor(user_board, mine_board, x, y)
			else:
				user_board[x][y] = mine_board[x][y]
				print('Dusty uncovered cell at %d,%d',x,y)
				#printBoard(user_board)
				continue

	## recursively_traverse_neighbors - function uncovers all neighbors surronding a cell
	##
	## paramets -
	##		user_board - board of 'A', avaiable, or integers >= 0
	##		mine_board - an integer >=0 and <= 8 is number of mines surronding, a cell with a 9 indicates a mine, game over
	##		myset - list of x,y coordinates that we havve uncovered
	## 		zero - list of x,y coordaintes that have a 0 (not surrounding it)
	def recursively_traverse_neighbors(self, user_board, mine_board, myset, zero):
		x = [-1, -1, -1 , 0, 0, 1, 1, 1]
		y = [-1, 0, 1, -1, 1, -1, 0, 1]

		my_zero = []

		for point in zero:
			r = point[0]
			c = point[1]
			print('Dusty looked at the cell %d,%d and found that it has no mines in its neighbors. Dusty will now open up its neighbors.' , r, c)
			for z in range(0,8,1):
				temprow = point[0] + x[z]
				tempcol = point[1] + y[z]
				q = [temprow,tempcol]

				if temprow >= 0 and temprow < len(mine_board) and tempcol >= 0 and tempcol < len(mine_board[0]) and (q not in myset):
					if mine_board[temprow][tempcol] == 0:
						user_board[temprow][tempcol] = mine_board[temprow][tempcol]
						myset.append(q)
						my_zero.append(q)
					else:
						user_board[temprow][tempcol] = mine_board[temprow][tempcol]
						myset.append(q)
		if len(my_zero) == 0:
			return
		else:
			return self.recursively_traverse_neighbors(user_board, mine_board, myset, my_zero)

### set up some search to get a cluster
### 1 in a corner. randomly.
### 1 in an egde still go randomly
### number of un opened neighbor = number they gave us

	## random_neighbors - function will uncover a random neighbor of a cell
	## parameters -
	##		user_board - board of 'A', avaiable, or integers >= 0 indicating number of mindes in its neighbors
	##		mine_board - an integer >=0 and <= 8 is number of mines surronding,
	##						 a cell with a 9 indicates a mine, game over
	## 		row - row of the neighbors to uncover
	## 		col - col of the neighbors to uncover
	def random_neighbor(self,user_board, mine_board, row, col):
		x = [-1, -1, -1 , 0, 0, 1, 1, 1]
		y = [-1, 0, 1, -1, 1, -1, 0, 1]
		random_neigh = random.randint(0,7)
		row += x[random_neigh]
		col += y[random_neigh]
		if row >= 0 and row < len(mine_board) and col >= 0 and col < len(mine_board[0]):
			if mine_board[row][col] == 9:
				game_loss(user_board, mine_board, row ,col)
			else:
				print('Dusty will now uncover cell at %d,%d',row,col)
				user_board[row][col] = mine_board[row][col]
				# printBoard()

	## isEdge - returns boolean whether cell is egde or not
	## parameters -
	##		user_board - board of 'A', avaiable, or integers >= 0 indicating number of mindes in its neighbors
	##		mine_board - an integer >=0 and <= 8 is number of mines surronding,
	##						 a cell with a 9 indicates a mine, game over
	## 		row - row of the neighbors to uncover
	## 		col - col of the neighbors to uncover
	def isEdge(self,user_board, mine_board, row, col):
		x = [-1, -1, -1 , 0, 0, 1, 1, 1]
		y = [-1, 0, 1, -1, 1, -1, 0, 1]
		edgeCount = 0

		for i in range(0,8,1):
			temprow = row + x[i]
			tempcol = col +y[i]
			if row >= 0 and row < len(mine_board) and col >= 0 and col < len(mine_board[0]):
				edgeCount+=1

		if edgeCount == 5:
			return True
		else:
			return False

	## isCorner - returns boolean whether cell is egde or not
	## parameters -
	##		user_board - board of 'A', avaiable, or integers >= 0 indicating number of mindes in its neighbors
	##		mine_board - an integer >=0 and <= 8 is number of mines surronding,
	##						 a cell with a 9 indicates a mine, game over
	## 		row - row of the neighbors to uncover
	## 		col - col of the neighbors to uncover
	def isCorner(self,user_board, mine_board, row, col):
		x = [-1, -1, -1 , 0, 0, 1, 1, 1]
		y = [-1, 0, 1, -1, 1, -1, 0, 1]
		edgeCount = 0

		for i in range(0,8,1):
			temprow = row + x[i]
			tempcol = col +y[i]
			if row >= 0 and row < len(mine_board) and col >= 0 and col < len(mine_board[0]):
				edgeCount+=1

		if edgeCount == 3:
			return True
		else:
			return False

	def test_print_set(self, my_set):
		print('Printing set....')
		for i in my_set:
			print('(%d,%d)',(i.getX(),i.getY()))

	def test_print_list(self, my_list):
		print('Printing list....')
		for i in my_list:
			print('(%d,%d)',(i.getX(),i.getY()))



