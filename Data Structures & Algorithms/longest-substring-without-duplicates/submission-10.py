class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct={}
        p1=p2=0
        maxS=0
        while p1<len(s):
            if s[p1] not in dct:
                dct[s[p1]]=1
                p1+=1
            else:
                del dct[s[p2]]
                p2+=1
            maxS=max(maxS,p1-p2)

        return maxS
            