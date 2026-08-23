class Solution:
    def trap(self, height: List[int]) -> int:
        low=0
        high=len(height)-1
        leftMax=height[low]
        rightMax=height[high]
        total=0
        while low<high:
            if leftMax<rightMax:
                low+=1
                leftMax=max(leftMax,height[low])
                total+=leftMax-height[low]
            else:
                high-=1
                rightMax=max(rightMax,height[high])
                total+=rightMax-height[high]
        return total


