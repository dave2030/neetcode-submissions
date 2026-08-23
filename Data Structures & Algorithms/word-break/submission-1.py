class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False] * (len(s)+1)
        dp[len(s)]=True
        for x in range(len(s)-1,-1,-1):
            for w in wordDict:
                if x + len(w) <=len(s) and s[x:x+len(w)]==w and dp[x+len(w)]:
                    dp[x]=True
                    break
        return dp[0]