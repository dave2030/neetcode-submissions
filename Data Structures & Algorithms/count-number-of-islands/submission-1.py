class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows=len(grid)
        cols=len(grid[0])
        seen=set()
        length=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1" and (r,c) not in seen:
                    self.dfs(r,c,seen,grid)
                    length+=1
        return length

    
    def dfs(self,r,c,seen,grid):
        if min(r,c)<0 or r==len(grid) or c==len(grid[0]) or (r,c) in seen or grid[r][c]=="0":
            return 0



        seen.add((r,c))

        self.dfs(r,c+1,seen,grid)
        self.dfs(r+1,c,seen,grid)
        self.dfs(r,c-1,seen,grid)
        self.dfs(r-1,c,seen,grid)

        













