class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedL=sorted(range(len(position)), key=lambda i:position[i], reverse=True)
        
        res,prv=0,0
        for x in sortedL:
            if (target-position[x])/speed[x]>prv:
                res+=1
                prv=(target-position[x])/speed[x]
        return res