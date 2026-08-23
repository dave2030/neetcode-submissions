class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lSet=set()
        p1,p2=0,0
        maxS=0
        while p1<len(s):
            if s[p1] not in lSet:
                lSet.add(s[p1])
                p1+=1
            else:
                lSet.remove(s[p2])
                p2+=1
            maxS=max(maxS,p1-p2)
        return maxS