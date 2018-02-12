import numpy as np
import math
import itertools as itt
import copy as cp
import types
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
Dimy = len(field)
Dimx = len(field[0])

#The following set of functions takes an index of a cleared cell
#and returns a list of adjacent cells that have unknown status. If the index is
#of an unknown cell, an empty list is returned. 


#This function builds the list of unknown neighbors
def unknownsadder (neighborslist, y, x):
    for adjy in y:
        for adjx in x:
            if status[adjy][adjx] == 'u':
                neighborslist = neighborslist + [[adjy,adjx]]
    return neighborslist


#These two functions check what part of the board the requested cell is in. 
def cornerchecker(y,x):
    if (y == 0 and x == 0):
        return 'UL'
    elif (y == 0 and x == Dimx-1):
        return 'UR'
    elif (y == Dimy-1 and x == 0):
        return 'LL'
    elif (y == Dimy-1 and x == Dimx-1):
        return 'LR'
    else:
        return 'False'
def boundarychecker(y,x):
    if (y < 0 or y > Dimy-1) or (x<0 or x>Dimx-1):
        return 'Invalid Location'
    elif y == 0:
        if cornerchecker(y,x) == 'False':
            return 'Top'
        else:
            return cornerchecker(y,x)
    elif y == Dimy-1:
        if cornerchecker(y,x) == 'False':
            return 'Bottom'
        else:
            return cornerchecker(y,x)
    elif x == 0:
        if cornerchecker(y,x) == 'False':
            return 'Left'
        else:
            return cornerchecker(y,x)
    elif x == Dimx-1:
        if cornerchecker(y,x) == 'False':
            return 'Right'
        else:
            return cornerchecker(y,x)
    else:
        return 'Center'
#This function determines the appropriate range of adjacent indexes based on
#the section of the board
def neighborsrange(y,x):
    yloc = y
    xloc = x
    section = boundarychecker(y,x)
    if section in ('UL', 'UR', 'Top'):
        yrange = range(y, y+2)
        if section == 'UL':
            xrange = range(x, x+2)
        elif section == 'UR':
            xrange = range(x-1,x+1)
        elif section == 'Top':
            xrange = range(x-1,x+2)
    elif section in ('LL', 'LR', 'Bottom'):
        yrange = range(y-1, y+1)
        if section == 'LL':
            xrange = range(x, x+2)
        elif section == 'LR':
            xrange = range(x-1,x+1)
        elif section == 'Bottom':
            xrange = range(x-1,x+2)
    elif section == 'Left':
        yrange = range(y-1,y+2)
        xrange = range(x, x+2)
    elif section == 'Right':
        yrange = range(y-1,y+2)
        xrange = range(x-1,x+1)
    elif section == 'Center':
        xrange = range(x-1,x+2)
        yrange = range(y-1,y+2)
    else:
        return 'Invalid Location'
    return [yrange, xrange]                

#This is the main function that creates the list of unknown neighbors to a cell
#Arguments are row coordinate, column coordinate. Output is a list, where each
#entry is a list of the [row coordinate, column coordinate] of a
#neighbor of unknown status.
def neighborhood (y,x):
    unknowns = []
    adjacents = neighborsrange(y,x)
    if isinstance(adjacents, list):  
        xadjs = adjacents[1]
        yadjs = adjacents[0]
        if status[y][x] == 'c':
            unknowns = unknownsadder(unknowns, yadjs, xadjs)
    else:
        return 'Invalid Location'
    return unknowns


    
                
    
    
