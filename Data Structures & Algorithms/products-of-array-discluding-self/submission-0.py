class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1 for x in range(len(nums))]
        for x in range(1,len(res)):
            res[x]=res[x-1]*nums[x-1]
        temp=1
        for x in range(len(res)-1,-1,-1):
            res[x]*=temp
            temp*=nums[x]
        return res



        #1,2,4,6
        #1,1,2,8
        #48,24,12,8