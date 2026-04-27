def solveSudoku(board):
    def is_valid(board,row,col,num):
        for j in range(9):
            if board[row][j]==num:
                return False
        for i in range(9):
            if board[i][col]==num:
                return False
            start_row=(row//3)*3
            start_col=(col//3)*3
            for i in range(3):
                for j in range(3):
                    if board[start_row+i][start_col+j]==num:
                        return False
            return True
    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    for num in "123456789":
                        if is_valid(board,i,j,num):
                            board[i][j]=num
                            if backtrack():
                                return True
                            board[i][j]="."
                    return False
        return True
    backtrack()
    return board
board=[
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
solution=solveSudoku(board)
for row in solution:
    print(row)
        
            
        
