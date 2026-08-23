class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res=[0]*26
        for x in range(len(s)):
            res[ord(s[x])-ord('a')]+=1
        for x in range(len(t)):
            res[ord(t[x])-ord('a')]-=1
        for x in res:
            if x!=0:
                return False
        return True
