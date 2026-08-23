class Solution:
    def trap(self, height: List[int]) -> int:
        prefix=[0] * len(height)
        postfix=[0]*len(height)
        prefix[0]=height[0]
        postfix[-1]=height[-1]
        for x in range(1,len(height)):
            prefix[x]=max(prefix[x-1],height[x])
        for x in range(len(height)-2,-1,-1):
            postfix[x]=max(postfix[x+1],height[x])
        res=0
        for x in range(len(height)):
            res+=min(prefix[x],postfix[x])-height[x]
        return res
