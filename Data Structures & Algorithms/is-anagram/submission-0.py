class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        d1,d2={},{}
        for x in range(len(s)):
            d1[s[x]]=d1.get(s[x],0)+1
            d2[t[x]]=d2.get(t[x],0)+1
        return d1==d2
        
            