class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=1
        ind=nums[0]
        for x in range(1,len(nums)):
            if nums[x]!=ind:
                ind=nums[x]
                nums[res]=nums[x]
                res+=1
        return res

