class Solution {
    public void rotate(int[] nums, int k) {
        k = k%nums.length;
        if(nums.length%2==0){
        for(int i=0;i<k;i++){
            int temp=nums[i];
            nums[i]=nums[i+k];
            nums[i+k]=temp;
        }
        }else{
            for(int i=0;i<k;i++){
            int temp=nums[i];
            nums[i]=nums[i+k+1];
            nums[i+k+1]=temp;
        }

    }
    }
}