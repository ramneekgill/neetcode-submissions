class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r_flag = 0
        c_flag = 0
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                r_flag = 1
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                c_flag = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        
        if r_flag:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if c_flag:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        
        