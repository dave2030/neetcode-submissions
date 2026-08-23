class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        rt=[]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
  

        def dfs(i,digits,tmp):
            if i==len(digits):
                rt.append(tmp)
                return
            
            for digit in digitToChar[digits[i]]:
                dfs(i+1,digits,tmp+digit)
        if digits:
            dfs(0,digits,"")
        return rt
        
