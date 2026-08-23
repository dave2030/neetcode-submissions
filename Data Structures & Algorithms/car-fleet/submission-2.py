class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedL=[]
        
        for x in range(len(position)):
            sortedL.append([position[x],speed[x]])
        sortedL.sort(key=lambda x:x[0], reverse=True)
        res,prv=0,0
        for p,s in sortedL:
            if (target-p)/s>prv:
                res+=1
                prv=(target-p)/s
        return res