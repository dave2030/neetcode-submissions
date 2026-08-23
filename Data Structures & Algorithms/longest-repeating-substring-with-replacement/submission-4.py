class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hSet={}
        maxF=0
        left=0
        res=0
        for right in range(len(s)):
            hSet[s[right]]=1 + hSet.get(s[right],0)
            maxF=max(maxF,hSet[s[right]])
            if right-left + 1 - maxF<=k:
                res=max(res,right-left+1)
            else:
                hSet[s[left]]-=1
                left+=1
        return res

