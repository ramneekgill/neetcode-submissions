class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for r in range(n)]
        col = set()
        pos_diag = set()
        neg_diag = set()
        
        def backtrack(r):
            if r==n:
                res.append([''.join(rw) for rw in board])
                return
            
            for c in range(n):
                if c in col or (r-c) in neg_diag or (r+c) in pos_diag:
                    continue
                col.add(c)
                neg_diag.add(r-c)
                pos_diag.add(r+c)
                board[r][c] = 'Q'
                backtrack(r+1)
                col.remove(c)
                neg_diag.remove(r-c)
                pos_diag.remove(r+c)
                board[r][c] = '.'
        backtrack(0)
        return res

        