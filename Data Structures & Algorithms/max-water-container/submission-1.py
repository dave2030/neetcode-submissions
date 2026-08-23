class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low=0
        high=len(heights)-1
        maxArea=0
        while low<high:
            minHeight=min(heights[low],heights[high])
            maxArea=max(maxArea,minHeight*(high-low))
            if heights[low]<maxArea:
                low+=1
            else:
                high-=1
        return maxArea
