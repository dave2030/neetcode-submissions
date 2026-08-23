class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        p1,p2=0,0
        maxF=0
        res=0
        while p1<len(s):
            count[s[p1]]=1+ count.get(s[p1],0)
            maxF=max(maxF,count[s[p1]])
            if p1 -p2 + 1 - maxF <=k:
                res=max(res,p1-p2+1)
            else:
                count[s[p2]]-=1
                p2+=1
            p1+=1
        return res


        

            