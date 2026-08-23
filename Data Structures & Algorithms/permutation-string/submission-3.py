class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        p1=p2=0
        c1=[0 for x in range(26)]
        c2=[0 for x in range(26)]
        for x in range(len(s1)):
            c1[ord(s1[x]) - ord('a')]+=1
            c2[ord(s2[x])- ord('a')]+=1
        if c1==c2:
            return True
        for x in range(len(s1),len(s2)):
            c2[ord(s2[x]) - ord('a')]+=1
            c2[ord(s2[x-len(s1)]) - ord('a')]-=1
            if c1==c2:
                return True


        return False
        