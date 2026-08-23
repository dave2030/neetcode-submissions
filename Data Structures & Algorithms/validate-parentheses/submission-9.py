class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = { ")" : "(", "]" : "[", "}" : "{" }
        for x in s:
            if x in "({[":
                stack.append(x)
            else:
                if not stack or pairs.get(x)!=stack[-1]:
                    return False
                stack.pop()
        return True if len(stack)==0 else False
                
