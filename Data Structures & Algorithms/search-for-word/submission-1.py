class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def rec(i, j, k):
            if k == len(word):
                return True
                
            if (i < 0 or i + 1 > rows
                or j < 0 or j + 1 > cols
                or board[i][j] != word[k] 
                or (i,j) in visited):
                return False
            
            visited.add((i, j))

            found = (rec(i+1, j, k+1) or
                     rec(i, j+1, k+1) or
                     rec(i-1, j, k+1) or
                     rec(i, j-1, k+1))

            visited.remove((i,j))

            return found

        for i in range(rows):
            for j in range(cols):
                if rec(i, j, 0):
                    return True

        return False