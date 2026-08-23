class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count=[0] * 26
        for x in s:
            count[ord(x)-ord('a')]+=1
        st=""
        for x in order:
            while count[ord(x)-ord('a')]>0:
                st+=x
                count[ord(x)-ord('a')]-=1
        for x in range(len(count)):
            while count[x]>0:
                st+=chr(x + ord('a'))
                count[x]-=1
        return st

