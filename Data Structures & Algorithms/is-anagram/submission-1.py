class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        occ=[0 for x in range(26)]
        for x in range(len(s)):
            occ[ord(s[x]) - ord('a')]+=1
            occ[ord(t[x]) - ord('a')]-=1
        for x in occ:
            if x!=0:
                return False
        
        return True
            