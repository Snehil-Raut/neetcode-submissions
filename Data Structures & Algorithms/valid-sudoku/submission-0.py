class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in board:
            row_check = set()
            for s in range(len(x)):
                if x[s]==".":
                    continue
                if x[s] not in row_check:
                    row_check.add(x[s])
                else:
                    return False
        
        for col in range(9):
            col_check  = set()
            for y in board:
                if y[col] == ".":
                    continue
                if y[col] not in col_check:
                    col_check.add(y[col])
                else:
                    return False

        for box_row_s in range(0,9,3):
            for box_col_s in range(0,9,3):

                row_col = set()
                
                for row_check in range(3):
                    for col_check in range(3):
                        row = box_row_s + row_check
                        col = box_col_s + col_check
                        
                        value = board[row][col]
                        if(value == "."):
                            continue
                        if(value not in row_col):
                            row_col.add(value)
                        else:
                            return False
        return True
        