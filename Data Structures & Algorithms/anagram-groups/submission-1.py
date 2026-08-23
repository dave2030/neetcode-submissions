class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct=collections.defaultdict(list)
        for x in strs:
            dct["".join(sorted(x))].append(x)
        return dct.values()