#from gui import MazeUI
#from maze_generator import MazeGenerator
from GenerateBoard import GenerateBoardUI
#from GenerateBoard import *
from Minesweeper import Minesweep
from GameState import *

# ### Generate 2dMaze where M is mine and 0 is not mined
# def generateBoard(MAZESIZE, PROBABILITY):
# 	maze = []
# 	prob = PROBABILITY*100
# 	for i in range(0,MAZESIZE,1):
# 		inner = []
# 		for j in range(0,MAZESIZE,1):
# 			rand = random.randint (1, 100)
# 			if(rand < prob):
# 				inner.append("M")
# 			else:
# 				inner.append("0")
# 		maze.append(inner)

# 	return maze

# ## Print a clear version of maze
# def printBoard(maze):
# 	for row in maze:
# 		for j in row:
# 			print j,
    # 		print

def testGamePlay(maze):
    #root = Tk ()
    #grid = MazeUI (root)
    i = 0
    while( i < 5):
        r, c =  input("Please input the cell you want to uncover by space seperated integers.\n").split()
        maze[int(r)][int(c)] = 'U'
        printBoard(maze)

def main ():
    PROBABILITY = 0.2
    rows, cols = input("Please input the demensions of the board by a space seperated integers.\n").split()
    maze = GenerateBoardUI()
    mine_board = maze.gen_Mine_Board(rows, cols, PROBABILITY)
    user_board = maze.gen_user_Board(rows, cols)
    print("Board filled with mines")
    maze.printBoard(mine_board)
    print("User_board")
    maze.printBoard(user_board)
    r, c = input("Please input the cell you want to uncover by space seperated integers.\n").split()
    sweep = Minesweep()
    sweep.querry_cell(user_board, mine_board, r, c)
    maze.printBoard(user_board)
    #testGamePlay(maze)

if __name__ == "__main__":
    main()
