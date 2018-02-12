import copy
def combinations(target,cells):
     for i in range(len(cells)):
         new_target = copy.copy(target)
         new_data = copy.copy(cells)
         new_target.append(cells[i])
         new_data = cells[i+1:]
         print (new_target)
         combinations(new_target,new_data)

target = []
cells = ['a','b','c','d']
def getneighbors(grid, rowno, colno):
    gridsize = len(grid)
    neighbors = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (rowno + i) < gridsize and -1 < (colno + j) < gridsize:
                neighbors.append((rowno + i, colno + j))

    return neighbors


combinations(target,cells)
