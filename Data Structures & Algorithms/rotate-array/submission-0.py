class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)

        def reversal(s,i):
            while s<i:
                nums[s],nums[i]=nums[i],nums[s]
                s+=1
                i-=1
        reversal(0,len(nums)-1)
        print(nums)
        reversal(k,len(nums)-1)
        print(nums)

        reversal(0,k-1)
        return nums