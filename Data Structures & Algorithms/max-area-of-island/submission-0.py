class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        def bfs(x,y):
            d=deque()
            d.append((x,y))
            grid[x][y]=0
            res=1
            while d:
                r,c=d.popleft()
                for dr,dc in directions:
                    row=r+dr
                    col=c+dc
                    if min(row,col)<0 or row>=rows or col>=cols or grid[row][col]==0:
                        continue
                    res+=1
                    grid[row][col]=0
                    d.append((row,col))
            return res
                    


        maxArea=0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==1:
                    maxArea=max(maxArea,bfs(x,y))
                   
        return maxArea
        