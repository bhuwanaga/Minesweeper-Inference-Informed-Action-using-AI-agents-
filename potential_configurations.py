import numpy as np
import math
import itertools as itt
import copy as cp
import neighborhood_generator as ng

#The following set of functions will create a set of possible configurations
#of all unknown cells adjacent to the cell given as argument. The configurations
#are all possible ways the uknown cells could be mined/clear, based on the
#information available from the query array. The output format will be a list,
#where each entry in the list is a dictionary. Each of these dictionaries
#represents one possible configuration of the unknown, adjacent cells.
#the keys of the dictionaries are the [row,column] coordinates of the unknown
#cells, and the values are the conjectured status of mined/clear for that
#particular configuration.


#We first extract how many mines are adjacent to the argument cell
def dangernumber(y,x):
    threat = query[y][x]
    return threat
#call the function that creates a list of neighbors of unknown status

#initialize a prototype dictionary to represent one possible configuration
#of mined/clear for the unknown, adjacent cells. The configuratis is
#initialized to indicate all surroundings are clear. 
def configuration(y,x):
    configdict = {}
    potentials = ng.neighborhood(y,x)
    for i in range(len(potentials)):
        configdict.update({tuple(potentials[i]):'c'})
    return configdict

#Now create the list with the required number of copies of this dictionary. Then
#change the list so that each dictionary inside the list represents a different
#possible configuration of the unknown cells.
def configlist(y,x):
    conjectures = []
    potentials = ng.neighborhood(y,x)
    minenum = dangernumber(y,x)
    #The next line creates an iterable of all potentials_choose_minenum possible
    #configurations for the unknown cells in the neighborhood
    configcombos = itt.combinations(potentials, minenum)
    comboslist = list(configcombos)
    conjecturedict = configuration(y,x)
    #now create the copies of the dictionary, one for each potential configuration
    for i in range(len(comboslist)):
        conjectures.append(conjecturedict.copy())
    #now edit each dictionary so each represents a different possible configuration
    #of where the mines could be.
    for i in range(len(comboslist)):
        for key in comboslist[i]:
            conjectures[i][tuple(key)] = 'm'
    return conjectures


    

