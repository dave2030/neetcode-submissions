class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,v in enumerate(nums):
            if i>0 and v==nums[i-1]:
                continue
            low,high=i+1,len(nums)-1
            while low<high:
                total=v+ nums[low]+ nums[high]
                if total<0:
                    low+=1
                elif total>0:
                    high-=1
                else:
                    res.append([nums[i],nums[low],nums[high]])
                    low+=1
                    high-=1
                    while low<high and nums[low]==nums[low-1]:
                        low+=1
        return res
