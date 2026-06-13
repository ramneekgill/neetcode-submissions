class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        res = [False]
        def backtrack(r,c, cur):
            if (r,c) in visited or r >= len(board) or c >= len(board[0]) or r < 0 or c < 0:
                return
            visited.add((r,c))
            cur.append(board[r][c])
            if ''.join(cur) == word:
                res[0] = True
            backtrack(r+1,c,cur)
            backtrack(r,c+1,cur)
            backtrack(r-1,c,cur)
            backtrack(r,c-1,cur)
            cur.pop()
            visited.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                backtrack(r,c,[])
                visited = set()
        return res[0]

            


        