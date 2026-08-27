class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack=[]
        def recurse(l,r,s):
            if l==r==n:
                stack.append("".join(s))
                return 
            if l<n:
                s.append("(")
                recurse(l+1,r,s)
                s.pop()
            if r<l:
                s.append(")")
                recurse(l,r+1,s)
                s.pop()
        recurse(0,0,[])
        print(stack)
        return stack