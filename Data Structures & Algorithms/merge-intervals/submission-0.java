class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->Integer.compare(a[0],b[0]));
        List<int[]> res = new ArrayList<>();
        res.add(intervals[0]);
        for(int [] i: intervals){
            int start=i[0];
            int end=i[1];
            int previousEnd=res.get(res.size()-1)[1];
            if(start<=previousEnd){
                res.get(res.size()-1)[1]=Math.max(previousEnd,end);
            }else{
                res.add(new int[]{start,end});
            }
        }
        return res.toArray(new int[res.size()][]);
    }
}

//[[1,3],[1,5],[1,7]], [1,7]
