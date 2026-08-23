class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        res=[0 for x in range(26)]
        hMap={}
        for x in s:
            res[ord(x)-ord('a')]+=1
        for x in t:
            res[ord(x)-ord('a')]-=1
        for x in res:
            if x!=0:
                return False
        return True
