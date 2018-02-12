from random import randint
print("\n\n\n\n\n\n")
board = []
mines = []
board_row = 0
adj = 0
wrong = 0
while True:
    board_row = int(input ("number of rows"))
    if board_row > 10:
       print("too big!")
    elif board_row<5:
       print("too small!")
    else:
       break

if board_row >=8:
    for i in range(15):
        mines.append([randint(0,board_row-1),randint(0,board_row-1)])
elif board_row>=5:
    for i in range(10):
        mines.append([randint(0,board_row-1),randint(0,board_row-1)])
for i in range (board_row):
    board.append(["X"]* board_row)
def draw_board(board):
    for i in board:
        print("".join(i))
def check_ans():
    if row > board_row or col > board_row:
        print("number is too high",board_row-1)
        wrong = 1
    else:
        wrong = 0

def adj_mines(r,c,adj):
    adj = 0
    if [r+1,c] in mines:
        adj+1
    if [r+1,c+1] in mines:
        adj+1
    if [r,c+1] in mines:
        adj+1
    if [r-1,c+1] in mines:
        adj+1
    if [r-1,c] in mines:
        adj+1
    if [r-1,c-1] in mines:
        adj+1
    if [r,c-1] in mines:
        adj+1
    if [r+1,c-1] in mines:
        adj+1
    return adj
draw_board(board)
while True:
    row = int (input("Row:"))
    col = int (input("Column:"))
    check_ans()
    if wrong!=1:
        if[row,col] in mines:
            break
        else:
            board[row][col] = str(adj_mines(row,col,0))
    draw_board(board)
print("sorry dusty is destroyed:(")
        


        
        
                            
