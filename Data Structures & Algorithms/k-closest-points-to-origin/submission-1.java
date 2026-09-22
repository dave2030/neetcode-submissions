class Solution {
    public int[][] kClosest(int[][] points, int k) {
        List<int[]> res = new ArrayList<>();
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a,b)->Integer.compare(a[0],b[0]));

        for(int [] p:points){
            int eucDist=p[0]*p[0] + p[1]*p[1];
            int result=(int) eucDist;
            minHeap.offer(new int[]{result,p[0],p[1]});
        }
        while(!minHeap.isEmpty() && k>0){
            int val[]=minHeap.poll();
            res.add(new int[]{val[1],val[2]});
            k-=1;
        }

        return res.toArray(new int[res.size()][]);

    }
}
