class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = defaultdict(int)
        for ch in t:
            tCount[ch] += 1

        res = ""
        resLen = float("inf")
        l = 0
        currCount = defaultdict(int)
        need = len(tCount.keys())
        have = 0
        for r in range(len(s)):
            currCount[s[r]] += 1
            if s[r] in tCount and currCount[s[r]] == tCount[s[r]]:
                have += 1
                
            while have == need:
                if r - l + 1 < resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                currCount[s[l]] -= 1
                if s[l] in tCount and currCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        return res

    def check(self, cc, tc):
        for k, v in tc.items():
            if cc[k] < v:
                return False
        return True
