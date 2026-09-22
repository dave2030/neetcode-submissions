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
        intervals.sort((a,b)->Integer.compare(a.start,b.start));
        int max=0;
        PriorityQueue<int[]> rooms = new PriorityQueue<>((a,b)->Integer.compare(a[1],b[1]));
        for(Interval i:intervals){
            int start=i.start;
            int end=i.end;
            while(!rooms.isEmpty() && rooms.peek()[1]<=start){
                rooms.poll();
            }
            rooms.offer(new int[]{start,end});
            max=Math.max(rooms.size(),max);
            }

        
        return max;
    }

    }

