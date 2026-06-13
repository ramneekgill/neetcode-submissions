class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROWS, COLS = len(board)-1, len(board[0])-1
        def dfs(r,c):
            if (r<0 or c<0 or r>=len(board) or c>=len(board[0]) or
                (r,c) in visited or board[r][c] == 'X'):
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(len(board)):
            
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][COLS] == 'O':
                print("row: ", r)
                dfs(r,COLS)
        
        for c in range(len(board[0])):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[ROWS][c] == 'O':
                dfs(ROWS,c)
        print(visited)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'
        


        