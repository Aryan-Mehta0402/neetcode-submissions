class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            Hashrow = {}
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                Hashrow[board[i][j]] = 1 + Hashrow.get(board[i][j], 0)
                if Hashrow[board[i][j]] > 1:
                    return False

        # all columns should be 1,0
        for i in range(9):
            Hashcol = {}
            for j in range(9):
                val = board[j][i]
                if val == ".":
                    continue
                Hashcol[board[j][i]] = 1 + Hashcol.get(board[j][i], 0)
                if Hashcol[board[j][i]] > 1:
                    return False

        # all boxes should be 1,0
        box = {}
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                Hashbox = {}
            # inside one 3x3 box
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = board[r][c]

                        if val == ".":
                            continue
                        Hashbox[board[r][c]] = 1 + Hashbox.get(board[r][c], 0) 
                        if Hashbox[board[r][c]] > 1:
                            return False
        return True
        