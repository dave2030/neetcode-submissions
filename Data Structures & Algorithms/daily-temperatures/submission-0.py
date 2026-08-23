class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        res=[0] * len(temperatures)
        for x in range(len(temperatures)):
            while st and st[-1][1]<temperatures[x]:
                i,v=st.pop()
                res[i]=x-i
            st.append((x,temperatures[x]))
        return res


