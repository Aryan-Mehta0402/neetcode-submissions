class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # capture regions that are surrounded
        # how to identify surrounded regions?
        # first identify regions then 
        # check if it is connected to any edge 
        # if yes then cant replace it else irreplacable
        
        if not board:
            return
        
        edge_os = set()
        rows, cols = len(board), len(board[0])        

        def dfs(r, c):
            board[r][c] = "#"
            dirx = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in dirx:
                row, col = r + dr, c + dc
                if (-1 < row < rows and 
                   -1 < col < cols and 
                   board[row][col] == "O"):
                    dfs(row, col)

         # Top and bottom rows
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        # Left and right columns
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
            


