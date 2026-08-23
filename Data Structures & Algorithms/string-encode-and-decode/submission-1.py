class Solution:

    def encode(self, strs: List[str]) -> str:
        st=""
        for x in strs:
            st+= str(len(x)) + "!" + x
        return st

    def decode(self, s: str) -> List[str]:
        st=""
        ind=0
        res=[]
        while ind<len(s):
            tmp=ind
            while s[tmp]!="!":
                tmp+=1
            length=int(s[ind:tmp])
            ind=tmp+length+1
            res.append(s[tmp+1:ind])
            
        
        return res
        
        #["4","!","n","e","e","t","4","!","c","o","d","e","4","!","l","o","v","e","3","!","y","o","u"]




