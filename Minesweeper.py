from GameState import *

# check all neighbors for mines in mine_board and update user_board
# Possibly recusively do the neighbors neighbors if row,col == 0....??
class Minesweep():
	j = 0;

	def querry_cell(self, user_board, mine_board, row, col):
	# loop through all possible coordinates
		row = int(row)
		col = int(col)
		x = [-1, 0, 1, -1, 1, -1, 0, 1]
		y = [-1, -1, -1, 0, 0, 1, 1, 1]
		if mine_board[row][col] == 1:
			print("are we here")
			game_loss(user_board, mine_board, row ,col)
		else:
			mine_count = 0;
			for i in range(0,8,1):
				rw = row + x[i]
				cl = col + y[i]
				if rw >= 0 and rw < len(user_board) and cl >= 0 and cl < len(user_board[0]) and mine_board[rw][cl] == 1:
					mine_count += 1
			# if mine_count == 0:
			# 	if self.j>7:
			# 		return;
			# 	else:
			# 		rw = row + x[self.j]
			# 		cl = col + y[self.j]
			# 		if rw >= 0 and rw < len(user_board) and cl >= 0 and cl < len(user_board[0]):
			# 			return self.querry_cell(user_board, mine_board, rw + x[++self.j], cl + y[++self.j])
			# else:
			user_board[row][col] = mine_count
