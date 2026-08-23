class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]

        def combine(i,tmp):
            if len(tmp)==k:
                res.append(tmp.copy())
                return
            
            for x in range(i,n+1):
                tmp.append(x)
                combine(x+1,tmp)
                tmp.pop()

        combine(1,[])
        return res