class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        ops="+-*/"
        res=0
        for x in tokens:
            if x=="+":
                st.append(st.pop()+st.pop())
            elif x=="-":
                a=st.pop()
                b=st.pop()
                st.append(b-a)
            elif x=="*":
                st.append(st.pop()*st.pop())
            elif x=="/":
                a=st.pop()
                b=st.pop()
                st.append(int(b/a))
            else:
                st.append(int(x))
        return st[0]

                    
        