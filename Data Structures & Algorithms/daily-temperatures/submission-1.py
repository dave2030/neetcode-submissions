class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output=[0 for x in range(len(temperatures))]
        for x in range(len(temperatures)):
            while stack and stack[-1][1]<temperatures[x]:
                i,v=stack.pop()
                output[i]=x-i

            stack.append((x,temperatures[x]))
        return output
        