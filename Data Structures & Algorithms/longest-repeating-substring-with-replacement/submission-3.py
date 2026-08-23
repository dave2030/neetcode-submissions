class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1,p2=0,0
        dct={}
        maxS=0
        longest=0
        for p1 in range(len(s)):
            dct[s[p1]] = 1 + dct.get(s[p1],0)
            maxS=max(maxS,dct[s[p1]])
            if p1-p2+1 - maxS<=k:
                longest=max(longest,p1-p2+1)
            else:
                dct[s[p2]]-=1
                p2+=1
        return longest


        
                