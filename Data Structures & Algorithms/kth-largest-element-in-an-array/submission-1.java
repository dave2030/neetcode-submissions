class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        for(int i:nums){
            heap.offer(i);
        }
        int val=-1;
        while(!heap.isEmpty() && k>0){
            val=heap.poll();
            k-=1;
        }
        return val;
    }
}
