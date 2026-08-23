class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low=0
        high=len(heights)-1
        minArea=0
        total=0
        while low<high:
            minArea=min(heights[low],heights[high])
            total=max(total,minArea * (high-low))
            if heights[low]<heights[high]:
                low+=1
            else:
                high-=1
        return total