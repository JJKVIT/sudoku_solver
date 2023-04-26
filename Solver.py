def sudoku(slist,row=0,column=0):
    if row == 8 and column == 9:
        for i in range(9):
            print(slist[i])
        return True
    if column == 9:
        row += 1
        column = 0
    if slist[row][column] != 0:
        return sudoku(slist,row,column+1)
    else:
        c_list = [slist[cn][column] for cn in range(9)]
        for num in range(1,10):
            if solve(slist,row,column,num,c_list):
                slist[row][column] = num
                if sudoku(slist, row, column+1):
                    pass
            slist[row][column] = 0
def solve(slist,row,column,number,collist):
    if number in collist or number in slist[row]:
        return False
    erow = row - row % 3
    ecolumn = column - column % 3
    for i in range(3):
        for p in range(3):
            if number == slist[erow+i][ecolumn+p]:
                return False
    return True
# format for input #
'''fin_list = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
               [0, 1, 0, 0, 0, 4, 0, 0, 0],
               [4, 0, 7, 0, 0, 0, 2, 0, 8],
               [0, 0, 5, 2, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 9, 8, 1, 0, 0],
               [0, 4, 0, 0, 0, 3, 0, 0, 0],
               [0, 0, 0, 3, 6, 0, 0, 7, 2],
               [0, 7, 0, 0, 0, 0, 0, 0, 3],
               [9, 0, 3, 0, 0, 0, 6, 0, 4]]'''
# sudoku(fin_list)
