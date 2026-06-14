class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]
                if cell == '.':
                    continue
                if cell in rows[i] or cell in cols[j] or cell in boxes[((i//3)*3 + j//3)]:
                    return False
                rows[i].add(cell)
                cols[j].add(cell)
                boxes[((i//3)*3 + j//3)].add(cell)
        return True