class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # lcp = ""
        # minLen = min(len(s) for s in strs)
        # numStrs = len(strs)
        # for i in range(minLen):
        #     e = strs[0][i]
        #     for s in strs[1:]:
        #         if e != s[i]:
        #             return lcp
        #     lcp += e
        # return lcp

        # lcp = ""
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return lcp
        #     lcp += strs[0][i]
        # return lcp


        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

