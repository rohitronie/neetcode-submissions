class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        for s in strs:
            strCode = [0]*26
            for c in s:
                strCode[ord(c) - ord('a')] += 1
            res[tuple(strCode)].append(s)
        return list(res.values())



        