class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needMap={}
        hasMap={}
        has=0
        p2=0
        res=[-1,-1]
        minLength=float("inf")
        for x in t:
            needMap[x]=1+needMap.get(x,0)
        
        need=len(needMap)

        if len(s)<len(t):
            return ""
        
        for p1 in range(len(s)):
            hasMap[s[p1]]=1+ hasMap.get(s[p1],0)

            if s[p1] in needMap and needMap[s[p1]]==hasMap[s[p1]]:
                has+=1
            while has==need:
                if minLength>p1-p2+1:
                    minLength=p1-p2+1
                    res=[p2,p1+1]
                hasMap[s[p2]]-=1
                if s[p2] in needMap and needMap[s[p2]]>hasMap[s[p2]]:
                    has-=1
                p2+=1
        i1,i2=res
        return s[i1:i2] 

            



