class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        minLen = min(len(s) for s in strs)
        numStrs = len(strs)
        for i in range(minLen):
            e = strs[0][i]
            for s in strs[1:]:
                if e != s[i]:
                    return lcp
            lcp += e
        return lcp

