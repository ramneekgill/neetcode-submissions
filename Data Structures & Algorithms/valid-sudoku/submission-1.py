class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                cell = board[r][c]
                if cell == '.':
                    continue
                square = (r//3)*3 + (c//3)
                if cell in rows[r] or cell in cols[c] or cell in sqrs[square]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                sqrs[square].add(cell)
        return True

        