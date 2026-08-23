class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        res=[]
        def dfs(i,s,tmp):
            if s==target:
                res.append(tmp[::])
                return
            if i>=len(nums) or s>target:
                return
            tmp.append(nums[i])
            dfs(i,s+nums[i],tmp)
            tmp.pop()
            dfs(i+1,s,tmp)
        dfs(0,0,[])
        return res
