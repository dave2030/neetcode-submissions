class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        int prefix=0;
        int res=0;
        map.put(0,1);
        for(int i:nums){
            prefix+=i;
            int complement=prefix-k;
            res+=map.getOrDefault(complement,0);
            map.put(prefix,map.getOrDefault(prefix,0)+1);

        }
        return res;
    }
}