import collections
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for x in words:
            inWord=True
            for y in x:
                if y not in allowed:
                    inWord=False
                    break
            if inWord:
                count+=1
        return count
                


        