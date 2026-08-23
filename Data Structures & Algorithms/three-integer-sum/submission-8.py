class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,v in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                low=i+1
                high=len(nums)-1
                while low<high:
                    value=nums[i] + nums[low] + nums[high]
                    if value==0:
                        res.append([nums[low],v,nums[high]])
                        low+=1
                        high-=1
                        while low<high and nums[low]==nums[low-1]:
                            low+=1
                    
                    elif value>0:
                        high-=1
                    else:
                        low+=1
        return res

                    