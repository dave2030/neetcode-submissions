class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        leftB="({["
        pairs={"(":")","{":"}","[":"]"}
        for l in s:
            if l in leftB:
                st.append(l)
            else:
                if not st:
                    return False
                else:
                    val = st.pop()
                    if not pairs.get(val)==l:
                        return False
        return st==[]