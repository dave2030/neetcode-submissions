class Solution:
    def reverse(self, x: int) -> int:
        tmp=x
        negative=False
   
        if tmp<0:
            negative=True
            tmp*=-1
        start=0
        while tmp>0:
            start=start*10 + (tmp%10)
            tmp=tmp//10
        if negative:
            start*=-1
        if start<= -2**31 or start>=2**31 -1:
            return 0    
        return start
