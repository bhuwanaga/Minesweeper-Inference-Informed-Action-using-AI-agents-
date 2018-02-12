from Neighborhoods import Neighborhood
import itertools as itt
from Peeker import Peeker
import copy

class Configurations(object):

    def __init__(self, query, stats):
        self.query = query
        self.stats = stats

#This function builds the list of unknown neighbors    
    def unknownsadder(self, neighborslist, y, x):
        if self.stats[y][x] == 'u':
            neighborslist = neighborslist + [[y, x]]
        self.neighborslist = neighborslist
        return self.neighborslist


#This is the main function that creates the list of unknown neighbors to a cell
#Arguments are row coordinate, column coordinate. Output is a list, where each
#entry is a list of the [row coordinate, column coordinate] of a
#neighbor of unknown status.
    
    def neighborhood(self, y ,x):
        unknowns = []
        adjacents = Peeker.BoundaryCheck(self, y, x, self.stats)
        if isinstance(adjacents, list):
            if self.stats[y][x] == 'c':
                for coord in range(len(adjacents)):
                    y = adjacents[coord][0]
                    x = adjacents[coord][1]
                    unknowns = self.unknownsadder(unknowns, y, x)
        else:
            return 'Invalid Location'
        self.unknowns = unknowns
        return self.unknowns
        



    def dangernumber(self, y, x):
        threat = self.query[y][x]
        self.threat = threat
        return self.threat


    def configuration(self, y, x):
        configdict = {}
        potentials = self.neighborhood(y,x)
        for i in range(len(potentials)):
            configdict.update({tuple(potentials[i]):'c'})
        self.configdict = configdict
        return self.configdict


    def configlist(self, y, x):
        conjectures = []
        if self.stats[y][x] == 'c':
            
            potentials = self.neighborhood(y,x)
            minenum = self.dangernumber(y,x)
            configcombos = itt.combinations(potentials, minenum)
            comboslist = list(configcombos)
            conjecturedict = self.configuration(y,x)
            for i in range(len(comboslist)):
                conjectures.append(conjecturedict.copy())
            for i in range(len(comboslist)):
                for key in comboslist[i]:
                    conjectures[i][tuple(key)] = 'm'
        self.conjectures = conjectures
        return self.conjectures
                
