"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:return intervals
        intervals.sort(key=lambda x:x.start)
        cEnd=intervals[0].end
        for x in range(len(intervals)):
            if x>0 and cEnd>=intervals[x].start:
                return False
            cEnd=intervals[x].end
        return True
