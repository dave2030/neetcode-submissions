class Solution {
    public void rotate(int[] nums, int k) {
        k = k%nums.length;
        for(int i=0;i<k;i++){
            int temp=nums[i];
            nums[i]=nums[i+k];
            nums[i+k]=temp;
        }
    }
}