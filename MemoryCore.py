import random
import numpy as np
import math
import copy as cp
#This class creates the three arrays that represent Dusty's basic knowledge of
#the board. This knowledge is:
    #Status - whether a cell is clear, mined, or unknown
    #Query - how many adjacent cells contain mines
    #Neighbors - how many adjacent cells have unknown status.
class MemoryCore(object):

    #Set the size of the board and playmode
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        #self.mode = mode

    #Create an array representing the knowledge of a cell
    #A cell is either clear, mined, or unknown
    #represented by 'c', 'm', or 'u'
    #As the board is initially unexplored, all values are initialized to 'u'
    def StatusArray(self):
        Status = np.empty((self.rows, self.cols), dtype=str)
        for i in range(self.rows):
            for j in range(self.cols):
                Status[i][j] = 'u'
        self.Status = Status
        return self.Status

    #Create an array representing the knowledge of how many adjacent cells
    #contain mines. If this number is unknown, the value of -1 is set.
    #As the board is initially unexplored, all values initialized to -1.
    def QueryArray(self):
        Query = np.empty((self.rows, self.cols), dtype=int)
        for i in range(self.rows):
            for j in range(self.cols):
                Query[i][j] = -1
        self.Query = Query
        return self.Query
    #Create an array representing the number of adjacent cells with unknown status
    #As the board is initially unexplored, the initial values are set to simply
    #Count the number of adjacent cells
    def NeighborsArray(self):
        Neighbors = np.empty((self.rows, self.cols), dtype=int)
        x = [-1,0,1,-1,1,-1,0,1]
        y = [-1,-1,-1,0,0,1,1,1]

        for i in range(0,self.rows,1):
            for j in range(self.cols):
                for z in range(8):
                    rw = i + y[z]
                    cl = j + x[z]
                    if rw >= 0 and rw < len(Neighbors) and cl>= 0 and cl <len(Neighbors[0]):
                        Neighbors[i][j] += 1
        self.Neighbors = Neighbors
        return self.Neighbors

        

        
