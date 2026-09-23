class Solution {
    Integer cache[];
    public int climbStairs(int n) {
        cache=new Integer[n+1];
        Arrays.fill(cache,0);
        return dfs(0,n);
    }

    public int dfs(int val,int n){
        if(val>n)return 0;
        if(val==n)return 1;
        if (cache[val]!=0)return cache[val];
        cache[val]=dfs(val+1,n) + dfs(val+2,n);
        return cache[val];
    }
        
}
