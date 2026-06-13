class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        while row < len(matrix):
            if target > matrix[row][-1]:
                row+=1
            else:
                break
        
        l, r = 0, len(matrix[0])
        while row < len(matrix) and l<=r:
            mid = l + (r-l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
            



        