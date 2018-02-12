import random
import numpy as np
import math
import copy as cp

#This class creates a minefield and a representation of the number of
#mined neighbor cells. To create a minefield, first create an instance.
#Second, call minefield to populate the mines.
#Third, call mined_neighbors_counter to create the representation of the
#dangerous cells adjacent.

class BoardGenerator(object):


    def __init__(self, rows, cols, prob):
        self.rows = rows
        self.cols = cols
        self.prob = prob

    def minefield(self):
        randfield = np.random.choice(2, size = (self.rows, self.cols), p=(1-self.prob, self.prob))
        self.gamefield = randfield
        return self.gamefield

    def mined_neighbors_counter(self):
        counter = cp.deepcopy(self.gamefield)
        x = [-1,0,1,-1,1,-1,0,1]
        y = [-1,-1,-1,0,0,1,1,1]

        for i in range(0,self.rows,1):
            for j in range(self.cols):
                if self.gamefield[i][j] == 0:
                    for z in range(8):
                        rw = i + y[z]
                        cl = j + x[z]
                        if rw >= 0 and rw < len(counter) and cl>= 0 and cl <len(counter[0]):
                            counter[i][j] += self.gamefield[rw][cl]
                if self.gamefield[i][j] == 1:
                    counter[i][j] = 9
        self.minecounter = counter
        return self.minecounter

    

    
