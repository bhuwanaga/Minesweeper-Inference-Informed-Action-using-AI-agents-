import random
import numpy as np
import math
import copy as cp
from MemoryCore import MemoryCore
from Peeker import Peeker
from Configurations import Configurations


class DustysBrain2(MemoryCore, Peeker):


    def __init__(self, rows, cols, game):
        MemoryCore.__init__(self, rows, cols)
        self.game = game
        self.stat = MemoryCore.StatusArray(self)
        self.quer = MemoryCore.QueryArray(self)
        self.nebs = MemoryCore.NeighborsArray(self)
        self.conf = Configurations(self.quer, self.stat)
        self.cleared = []
        self.kb = {}
        


    def Knowledge(self):
        self.stat = MemoryCore.StatusArray(self)
        self.quer = MemoryCore.QueryArray(self)
        self.nebs = MemoryCore.NeighborsArray(self)
        return self.stat, self.quer, self.nebs


    def UpdateKnowledge(self, row, col, game):
        Peeker.CheckCell(self, row, col, self.game, self.stat, self.quer, self.nebs)
        if self.game[row][col] < 9:
            self.cleared.append([row, col])
            self.conf = Configurations(self.quer, self.stat)
        elif self.game[row][col] == 9:
            print("I say you he dead")
        return self.stat, self.quer, self.nebs, self.conf, self.cleared

    def AddConjectures(self, conf, row, col):
        if ((row,col) not in self.kb) and (self.stat[row][col] == 'c'):
            self.kb.update({tuple((row,col)):self.conf.configlist(row,col)})
        return self.kb 
    
        
        

