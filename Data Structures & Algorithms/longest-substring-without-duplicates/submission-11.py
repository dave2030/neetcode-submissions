class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1,p2=0,0
        store=set()
        maxLength=0
        if len(s)<=1:
            return len(s)
        while p2<len(s):
            while s[p2] in store:
                store.remove(s[p1])
                p1+=1
            store.add(s[p2])
            maxLength=max(maxLength,p2-p1+1)
            p2+=1
        return maxLength

