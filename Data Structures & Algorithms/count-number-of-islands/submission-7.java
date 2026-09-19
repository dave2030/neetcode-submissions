class Solution {
    private static int directions [][]={{0,1},{1,0},{0,-1},{-1,0}};
    public int numIslands(char[][] grid) {
        int islands=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[i].length;j++){
                if(grid[i][j]=='1'){
                    bfs(i,j,grid);
                    islands+=1;
                }
            }
        }
        return islands;
    }

    private void bfs(int i,int j,char[][]grid){

        Queue<int[]> queue=new LinkedList<>();
        grid[i][j]='0';
        queue.add(new int[]{i,j});
        while(!queue.isEmpty()){
            int[]popleft=queue.poll();
            int row=popleft[0] , col=popleft[1];
            for(int direction[]:directions){
                int r=row+direction[0],c=col+direction[1];
                if(r<0||c<0||r>=grid.length||c>=grid[0].length||grid[r][c]=='0')continue;
                queue.add(new int[]{r,c});
                grid[r][c]='0';
            }
        }


        // if(i<0 || j<0 || i>=grid.length||j>=grid[i].length || grid[i][j]=='0')return;
        // grid[i][j]='0';
        
        // for(int row[]:directions){
        //     int r = i + row[0];
        //     int c= j + row[1];
        //     dfs(r,c,grid);
        // }
    } 
}
