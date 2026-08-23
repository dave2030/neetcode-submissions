class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for x in strs:
            res=res+str(len(x)) + "!" + x
        return res


    def decode(self, s: str) -> List[str]:
        res=[]
        p=0
        while p<len(s):
            i=p
            while s[i]!="!":
                i+=1
            length=int(s[p:i])
            i+=1
            res.append(s[i:i+length])
            p=i+length
        return res
            # if s[p]=="!":
            #     p+=1
            #     length=""
            #     while p<len(s) and s[p].isnumeric():
            #         length+=s[p]
            #         p+=1
            #     res.append(s[p,int(length)+p+1])
            #     p=int(length)+p+1
        return res


