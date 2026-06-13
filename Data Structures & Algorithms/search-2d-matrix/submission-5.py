class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l, r = 0, row*col-1
        while l<=r:
            m = l+(r-l)//2
            if matrix[m//col][m%col] == target:
                return True
            elif matrix[m//col][m%col] > target:
                r = m-1
            else:
                l = m+1
        return False

            



        