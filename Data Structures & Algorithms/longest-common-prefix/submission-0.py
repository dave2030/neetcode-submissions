class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=min(strs)
        length=len(min(strs))
        for x in strs:
            c=0
            while c<length:
                if x[c]!=prefix[c]:
                    prefix=x[:c]
                    length=len(prefix)
                c+=1
        # longest=
        # for x in strs:
        #     start=0
        #     while start<length:
        return prefix