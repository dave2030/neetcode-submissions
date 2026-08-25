class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct={}
        for i,v in enumerate(s):
            if v in dct:
                dct[v]=1000
            else:
                dct[v]=i
        res=1000
        for v in dct.values():
            res=min(res,v)
        return res if res!=1000 else -1


