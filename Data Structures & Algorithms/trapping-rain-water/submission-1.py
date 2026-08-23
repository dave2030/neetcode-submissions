class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxL=height[left]
        maxR=height[right]
        res=0
        while left<right:
            if height[left]<height[right]:
                if maxL>height[left]:
                    res+=maxL-height[left]
                else:
                    maxL=max(maxL,height[left])
                left+=1
            else:
                if maxR>height[right]:
                    res+=maxR-height[right]
                else:
                    maxR=max(maxR,height[right])
                right-=1

        
        return res



                
