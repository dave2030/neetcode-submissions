class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        islands=0
        def bfs(x,y):
            q=deque()
            q.append((x,y))
            grid[x][y]="0"
            while q:
                row,col=q.popleft()
                for x,y in directions:
                    r=row+x
                    c=col+y
                    if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]=="0":
                        continue
                    grid[r][c]="0"
                    q.append((r,c))

        # def dfs(x,y):
        #     if x<0  or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]=="0":
        #         return
        #     grid[x][y]="0"
        #     dfs(x+1,y)
        #     dfs(x,y+1)
        #     dfs(x-1,y)
        #     dfs(x,y-1)
            
            
                    
                    

                



        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y]=="1":
                    bfs(x,y)
                    islands+=1

    
        return islands

    

        
