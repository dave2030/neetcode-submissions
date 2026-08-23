class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        res=[-1,-1]
        needCount=len(t)
        hasMap={}
        needMap={}
        hasCount=0
        left=0
        minLength=float("inf")
        for x in t:
            needMap[x]=1+ needMap.get(x,0)
        for r in range(len(s)):
            hasMap[s[r]]=1+ hasMap.get(s[r],0)
            if s[r] in t and needMap[s[r]]>=hasMap[s[r]]:
                hasCount+=1
            while hasCount==needCount:
                if r+1-left<minLength:
                    minLength=r+1-left
                    res=[left,r+1]
                hasMap[s[left]]-=1
                if s[left] in needMap and hasMap[s[left]]<needMap[s[left]]:
                    hasCount-=1
                left+=1
        i1,i2=res
        return s[i1:i2]


