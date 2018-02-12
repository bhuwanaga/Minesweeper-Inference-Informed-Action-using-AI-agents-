import random
import Minesweeper

class GenerateBoardUI():

        # print board to terminal
        def printBoard(self,board):
                for row in board:
                        print(row)
        ## populate_mine_board - initializes the board with mines(indicated with a 9) and number of mines surronding a cell
        ## parameters -
        ##              rows - rows of the board
        ##              cols - cols of the board
        ##              prob - probability that a mine appears in the board
        def populate_mine_board(self, rows, cols, prob):
        # loop through all possible coordinates
                x = [-1, -1, -1 , 0, 0, 1, 1, 1]
                y = [-1, 0, 1, -1, 1, -1, 0, 1]
                # if mine_board[row][col] == 1:
                #       #print 'are we here'
                #       game_loss(user_board, mine_board, row ,col)
                # else:
                #       mine_count = 0; 
                #       for i in range(0,8,1):
                #               rw = row + x[i]
                #               cl = col + y[i]
                #               if rw >= 0 and rw < len(user_board) and cl >= 0 and cl < len(user_board[0]) and mine_board[rw][cl] == 1:
                #                       mine_count += 1
                #       user_board[row][col] = mine_count
                rows = int(rows)
                cols = int(cols)
                prob = float(prob)
                mine_board = []
                prob = prob*100
                for i in range(0,rows,1):
                        mine_inner = []
                        for j in range(0,cols,1):
                                rand = random.randint (1, 100)
                                if(rand < prob):
                                        mine_inner.append(9)
                                else:
                                        mine_inner.append(0)
                        mine_board.append(mine_inner)

                self.printBoard(mine_board)

                for i in range(0,rows,1):
                        for j in range(0,cols,1):
                                if mine_board[i][j] != 9:
                                        mine_count = 0
                                        for z in range(0,8,1):
                                                rw = i + x[z]
                                                cl = j + y[z]
                                                if rw >= 0 and rw < len(mine_board) and cl >= 0 and cl < len(mine_board[0]) and mine_board[rw][cl] == 9:
                                                        mine_count += 1
                                        mine_board[i][j] = mine_count

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

