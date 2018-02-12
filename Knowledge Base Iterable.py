import numpy as np
import math
import itertools as itt
import copy as cp
#first create a fixed minefield to test
field = np.array([[0, 0, 0, 0, 0],
                  [1, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 0, 1, 0]])

#Now create text examples of the three core memory arrays: status holds the
#status of a cell on the board. 'c' stands for clear,
#which means queried and no mine found
#'u' means unknown, so the cell hasn't been queried yet
#'m' means Dusty has determined a mine is in that cell

status = np.array([['c', 'c', 'c', 'u', 'u'],
                   ['u', 'u', 'u', 'u', 'u'],
                   ['c', 'c', 'c', 'u', 'u'],
                   ['u', 'u', 'u', 'c', 'c'],
                   ['u', 'u', 'u', 'u', 'u']])

#query stores the number that is returned when a safe cell is queried, which
#indicates how many of the adjacent cells contain mines

query = np.array([[1, 1, 1, 9, 9],
                 [9, 9, 9, 9, 9],
                 [1, 3, 3, 9, 9],
                 [9, 9, 9, 2, 1],
                 [9, 9, 9, 9, 9]])
#neighbors contains the number of adjacent cells with unknown status
neighbors = np.array([[2, 3, 4, 8, 8],
                      [8, 8, 8, 8, 8],
                      [4, 6, 6, 8, 8],
                      [8, 8, 8, 6, 4],
                      [8, 8, 8, 8, 8]])


#print out the test minefield and memory arrays
#print(field)
#print(status)
#print(query)
#print(neighbors)
#store the dimensions of the field
Dimy = len(field)
Dimx = len(field[0])

#now start creating a list of unknown neighbors for the cell indicated by index
#this is the cell's neighborhood
neighborhoods = [[]
for neby in Dimy:
    for nebx in Dimx:
        neighborhoodxy = []
#index = [2,2]
#xloc = index[0]
#yloc = index[1]
#neighborhood = []
        if (neby != (0 or Dimy-1) and nebx != (0 or Dimx-1))
            for i in range(neby-1, neby+2):
                for j in range(nebx-1, nebx+2):
                    if status[i][j] == 'u':
                        neighborhoodxy = neighborhoodxy + [[i,j]]
            print(neighborhoodxy)

#extract the number of potential mines adjacent to the indexed cell
                    maybeminesvalxy = query[neby][nebx]
#generate the combinations of possible configurations for the neighborhood
#the number of possible configurations will be neighborhood_choose_maybeminesval 
                    maybeminestuplexy = itt.combinations(neighborhoodxy, maybeminesvalxy)
                    maybemineslistxy = (list(maybeminestuplexy))

#print(maybemineslist)
#maybeminesone = maybemineslist[0]

#make a copy of the neighborhood. Might not be necessary; depends on if the
#neighborhood list will be modified or not.
#neighborhoodcopy = cp.deepcopy(neighborhood)

#build an initial dictionary of the neighborhood. Keys are tuples of the unknown
#cells' indices, values are initialized as 'c' for clear
                    propositiondictxy = {}
                    for i in range(len(neighborhoodcopyxy)):
                        propositiondict.update({tuple(neighborhoodcopy[i]):'c'})

#now create a list of copies of the dictionary. The number of copies will be
#neighborhood_choose_maybeminesval, one for each possible configuration. Then
#use the different combinations generated above to update the values for the
#corresponding copies of the dictionary. This will generate all
#neighborhood_choose_maybeminesval possible configurations for the neighrborhood;
#the possible configurations are stored in a single list, while each
#configuration is a dictionary. The keys are tuples representing indices for an
#uknown cell, the values are the potential status of that cell.
propositionlist = []
for i in range(len(maybemineslist)):
    propositionlist.append(propositiondict.copy())
for i in range(len(maybemineslist)):
    for key in maybemineslist[i]:
        propositionlist[i][tuple(key)]='m'

print(propositionlist)
#check that the size is correct.
#len(propositionlist) should equal neighborhood_choose_maybeminesval
print(len(propositionlist))
