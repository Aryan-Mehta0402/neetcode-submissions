class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cur = ""
        flag = 0
        visited_hash = {}

        rows = len(board)
        cols = len(board[0])

        def backtrack(i, j):
            nonlocal cur
            nonlocal flag
            nonlocal visited_hash

            visited_hash[(i, j)] = 1 + visited_hash.get((i, j), 0)

            if visited_hash[(i, j)] > 1:
                visited_hash[(i, j)] -= 1
                return

            if flag == 1:
                visited_hash[(i, j)] -= 1
                return

            if cur[-1] != word[len(cur) - 1]:
                visited_hash[(i, j)] -= 1
                return

            if len(cur) == len(word):
                if cur == word:
                    flag = 1
                visited_hash[(i, j)] -= 1
                return

            if i + 1 < rows:
                cur += board[i + 1][j]
                backtrack(i + 1, j)
                cur = cur[:-1]

            if i - 1 >= 0:
                cur += board[i - 1][j]
                backtrack(i - 1, j)
                cur = cur[:-1]

            if j + 1 < cols:
                cur += board[i][j + 1]
                backtrack(i, j + 1)
                cur = cur[:-1]

            if j - 1 >= 0:
                cur += board[i][j - 1]
                backtrack(i, j - 1)
                cur = cur[:-1]

            visited_hash[(i, j)] -= 1

        for r in range(rows):
            for c in range(cols):
                cur = board[r][c]
                visited_hash = {}
                backtrack(r, c)

                if flag:
                    return True

        return False