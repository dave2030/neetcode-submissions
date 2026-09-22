/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        intervals.sort((a,b)->Integer.compare(a.start,b.end)); //Sort by start time in asc
        int previousEnd=-1;
        int res=1;
        for(Interval i:intervals){
            int start=i.start;
            int end=i.end;
            if(start>=previousEnd && previousEnd!=-1){
                res+=1;
            }
            previousEnd=end;
            
        }
        return res;
    }
}
