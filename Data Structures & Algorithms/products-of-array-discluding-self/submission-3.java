class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prefix=1;
        int[]res=new int[nums.length];
        Arrays.fill(res,1);
        for(int i=0;i<nums.length;i++){   
            res[i]=prefix;
            prefix*=nums[i];
        }
        int postfix=1;
        for(int i=nums.length-1;i>=0;i--){
            res[i]*=postfix;
            postfix*=nums[i];
        }
        return res;
    }
}  



// 1 1 2 4 6 1
// 1 1 1 2 8 1
// 1 1 2 8
//  48  24 12  8

// 48 24 12 8