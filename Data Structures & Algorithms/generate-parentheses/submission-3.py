class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        def backTrack(left,right,res):
            if left==right==n:
                stack.append("".join(res))

            if left<n:
                res.append("(")
                backTrack(left+1,right,res)
                res.pop()
            
            if right<left:
                res.append(")")
                backTrack(left,right+1,res)
                res.pop()

        backTrack(0,0,[])
        return stack