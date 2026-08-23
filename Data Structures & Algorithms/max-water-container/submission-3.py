class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low=0
        high=len(heights)-1
        totalM=0
        while low < high:
            totalM= max(totalM,min(heights[low],heights[high]) * (high-low))
            if heights[low]<=heights[high]:
                low+=1
            else:
                high-=1
        return totalM
