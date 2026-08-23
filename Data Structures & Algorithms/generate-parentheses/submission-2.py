class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        st=[]
        def generate(l,r):
            if l==r==n:
                res.append("".join(st))
                return
            if l<n:
                st.append("(")
                generate(l+1,r)
                st.pop()
            if r<l:
                st.append(")")
                generate(l,r+1)
                st.pop()
        generate(0,0)

        return res

           
