class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0]) - 1
        rows = len(matrix[0])

        while l <= r:
            m = (l + r)//2
            if matrix[m//rows][m%rows] == target:
                return True
            elif matrix[m//rows][m%rows] < target:
                l = m + 1
            else:
                r = m - 1

        return False
