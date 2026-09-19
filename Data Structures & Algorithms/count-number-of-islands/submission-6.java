class Solution {
    private static int directions [][]={{0,1},{1,0},{0,-1},{-1,0}};
    public int numIslands(char[][] grid) {
        int islands=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[i].length;j++){
                if(grid[i][j]=='1'){
                    dfs(i,j,grid);
                    islands+=1;
                }
            }
        }
        return islands;
    }

    private void dfs(int i,int j,char[][]grid){

        if(i<0 || j<0 || i>=grid.length||j>=grid[i].length || grid[i][j]=='0')return;
        grid[i][j]='0';
        
        for(int row[]:directions){
            int r = i + row[0];
            int c= j + row[1];
            dfs(r,c,grid);
        }
    } 
}
