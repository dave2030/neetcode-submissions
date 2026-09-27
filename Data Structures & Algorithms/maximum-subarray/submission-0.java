class Solution {
    public int maxSubArray(int[] nums) {

        int res=-1;
        int curSum=0;
        for(int i=0;i<nums.length;i++){
            if(curSum+nums[i]>=0){
                curSum+=nums[i];
                res=Math.max(res,curSum);

            }
            else{
                curSum=0;
            }
        }
        return res;
    }
}
