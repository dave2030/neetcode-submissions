class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        c1,c2=[0] *26 ,[0] * 26
        for x in range(len(s1)):
            c1[ord(s1[x])-ord('a')]+=1
            c2[ord(s2[x])-ord('a')]+=1
        if c1==c2:
            return True
        for x in range(len(s1),len(s2)):
            c2[ord(s2[x])-ord('a')]+=1
            c2[ord(s2[x-len(s1)])-ord('a')]-=1
            if c1==c2:
                return True       
        return False
        