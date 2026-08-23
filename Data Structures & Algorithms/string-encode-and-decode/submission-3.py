class Solution:

    def encode(self, strs: List[str]) -> str:
        st=""
        for x in strs:
            st+= str(len(x)) + "!" + x
        return st

    def decode(self, s: str) -> List[str]:
        res=[]
        p1=p2=0
        while p1<len(s):
            p2=p1
            while s[p2]!='!':
                p2+=1
            digit=int(s[p1:p2])
            p2+=1
            st=s[p2:p2+digit]
            p1=p2+digit
            res.append(st)
        return res
