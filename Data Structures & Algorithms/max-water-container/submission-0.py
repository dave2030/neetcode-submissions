class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low=0
        high=len(heights)-1
        maxA=0
        while low<high:
            area=(high-low) *min(heights[low],heights[high])
            maxA=max(maxA,area)
            if heights[low]<heights[high]:
                low+=1
            else:
                high-=1
        return maxA
        