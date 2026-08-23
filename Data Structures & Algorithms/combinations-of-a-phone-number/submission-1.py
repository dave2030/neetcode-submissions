class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        

        def backTrack(i,tmp):
            if len(tmp)==len(digits):
                res.append(tmp)
                return
            for x in digitToChar[digits[i]]:
                backTrack(i+1,tmp+x)



        if digits:
            backTrack(0,"")
        return res
