class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def subset(i,n,sub):
            if i==n:
                res.append(sub[::])
                return 
            else:
                sub.append(nums[i])
                subset(i+1,n,sub)
                sub.pop()
                subset(i+1,n,sub)

        subset(0,len(nums),[])
        return res