import random
import numpy as np
import math
import copy as cp
from Random_Board import BoardGenerator
from MemoryCore import MemoryCore

class Peeker(object):
    #this function checks the adjacency neighborhood of a cell, making sure
    #to stay within the boundaries of the board and not wrap around using
    #negative indices. The mode parameter determines what to do.
    

    def BoundaryCheck(self, i,j, board):
        x = [-1,0,1,-1,1,-1,0,1]
        y = [-1,-1,-1,0,0,1,1,1]
        x_ok = []
        y_ok= []
        for z in range(8):
            rw = i + y[z]
            cl = j + x[z]
            if 0 <= rw and  rw < len(board) and 0 <= cl and cl <len(board[0]):
                x_ok.append(cl)
                y_ok.append(rw)
        yx = [y_ok, x_ok]
        zipyx = list(map(list, zip(*yx)))
        return zipyx
   #This function counts how many neighbors have unknown status                         
    def NeighborIter(self, i,j, board, board2):
        x = [-1,0,1,-1,1,-1,0,1]
        y = [-1,-1,-1,0,0,1,1,1]
        board[i][j] = 0
        for z in range(8):
            rw = i + y[z]
            cl = j + x[z]
            if 0 <= rw and  rw < len(board) and 0 <= cl and cl <len(board[0]):
                if board2[rw][cl] == 'u':
                    board[i][j] += 1               
    #This function checks a cell. If there's a mine, prints "Boom"
    #If there is no mine, updates the primary memory arrays.
    def CheckCell(self, row, col, board, stats, quer, nebs):
        if board[row][col] == 9:
            print("Boom")
        elif board[row][col] < 9:
            stats[row][col] = 'c'
            quer[row][col] = board[row][col]
            nebupdate = self.BoundaryCheck(row,col,board)
            nebupdate.append([row, col])
            for i in range(len(nebupdate)):
                y = nebupdate[i][0]
                x = nebupdate[i][1]
                if stats[y][x] == 'c':
                    self.NeighborIter(y, x, nebs, stats)
