class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length=0
        rows=len(grid)
        cols=len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]

        def bfs(x,y):
            grid[x][y]="0"
            q=deque()
            q.append((x,y))
            while q:
                r,c=q.popleft()
                for dr,dc in directions:
                    row=r+dr
                    col=c+dc
                    if min(row,col)<0 or row>=rows or col>=cols or grid[row][col]=="0":
                        continue
                    q.append((row,col))
                    grid[row][col]="0"

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] =="1":
                    bfs(x,y)
                    length+=1
            



            
        return length
        













