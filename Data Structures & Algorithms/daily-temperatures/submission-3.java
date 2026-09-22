class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[]res=new int[temperatures.length];
        Arrays.fill(res,0);
        Deque<int[]> stack = new ArrayDeque<>();
        for(int i=0;i<temperatures.length;i++){
            while(!stack.isEmpty() && stack.peek()[0]<temperatures[i]){
                int[]entry=stack.pop();
                res[entry[1]]=i-entry[1];
            }
            
            stack.push(new int[]{temperatures[i],i});
            
        }
        return res;
    }
}
