class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        res=[]
        for x in s:
            if x!="]":
                stack.append(x)
            else:
                st=""
                while stack[-1]!="[":
                    st=stack.pop() + st
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                stack.append(int(num)*st)
        return "".join(stack)




