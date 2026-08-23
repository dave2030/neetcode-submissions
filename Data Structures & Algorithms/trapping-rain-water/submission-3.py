class Solution:
    def trap(self, height: List[int]) -> int:
        low=0
        high=len(height)-1
        maxLeft=height[low]
        maxRight=height[high]
        res=0
        while low<high:
            if maxLeft<maxRight:
                low+=1
                maxLeft=max(maxLeft,height[low])
                res+=maxLeft-height[low]
                
            else:
                high-=1
                maxRight=max(maxRight,height[high])
                res+=maxRight-height[high]
        return res