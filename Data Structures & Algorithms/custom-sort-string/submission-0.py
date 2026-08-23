class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hMap={}
        for x in range(26):
            hMap[x]=0
        for x in s:
            hMap[ord(x)-ord('a')]+=1
        st=""
        for x in order:
            while hMap[ord(x)-ord('a')]>0:
                st+=x
                hMap[ord(x)-ord('a')]-=1
        for k,v in hMap.items():
            while hMap[k]>0:
                st+=chr(k + ord('a'))
                hMap[k]-=1
        return st

