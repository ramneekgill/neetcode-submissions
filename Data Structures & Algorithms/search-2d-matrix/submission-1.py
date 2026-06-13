class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1
        while top <= bot:
            m_row = (top+bot)//2
            if target > matrix[m_row][-1]:
                top = m_row+1
            elif target < matrix[m_row][0]:
                bot = m_row-1
            else:
                break
        if (top > bot): 
            return False

        m_row = (top+bot)//2
        l, r = 0, len(matrix[0])-1
        while l<=r:
            mid = (l+r)//2
            if target > matrix[m_row][mid]:
                l = mid+1
            elif target < matrix[m_row][mid]:
                r = mid-1
            else:
                return True
        return False
        