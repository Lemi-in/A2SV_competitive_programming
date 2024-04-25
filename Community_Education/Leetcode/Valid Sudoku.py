class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        for _ in range(9):
            rows.append(set())
        cols = []
        for _ in range(9):
            cols.append(set())
        boxes = []
        for _ in range(9):
            boxes.append(set())
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    target = int(board[i][j])
                    if target in rows[i] or target in cols[j] or target in boxes[(i // 3) * 3 + (j // 3)]:
                        return False
                    rows[i].add(target)
                    cols[j].add(target)
                    boxes[(i // 3) * 3 + (j // 3)].add(target)

        return True
