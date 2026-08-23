class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        nines=collections.defaultdict(set)
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y]==".":
                    continue
                if board[x][y] in rows[x] or board[x][y] in cols[y] or board[x][y] in nines[(x//3,y//3)]:
                    return False            
                rows[x].add(board[x][y])
                cols[y].add(board[x][y])
                nines[(x//3,y//3)].add(board[x][y])
        return True
