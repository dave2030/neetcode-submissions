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
    public boolean canAttendMeetings(List<Interval> intervals) {
        intervals.sort((a,b)->Integer.compare(a.start,b.end));
        int previous=-1;
        for(Interval i:intervals){
            int start=i.start;
            int end=i.end;
            if(previous==-1)previous=end;
            else{
                if(start<previous)return false;
                previous=end;
            }
        }
        return true;
    }
}
