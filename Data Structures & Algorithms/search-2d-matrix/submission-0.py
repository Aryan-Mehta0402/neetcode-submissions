class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        rows = len(matrix)
        cols = len(matrix[0])
        r = rows*cols - 1

        while l <= r:
            m = l + (r-l)//2

            if matrix[m//cols][m%cols] == target:
                return True
            elif matrix[m//cols][m%cols] > target:
                r = m-1
            else:
                l = m+1

        return False
