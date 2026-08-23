class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        res=float("inf")
        while low<=high:
            # if nums[high]>nums[low]:
            #     res=nums[low]
            #     break
            mid =low + (high-low)//2
            res=min(res,nums[mid])
            if nums[mid]<=nums[high]:
                high=mid-1
            else:
                low=mid+1
        return res
