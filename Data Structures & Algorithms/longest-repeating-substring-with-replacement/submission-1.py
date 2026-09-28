class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        maxFreq = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])

            while (r+1 - l) - maxFreq > k:
                count[s[l]] -= 1
                l+=1
            
            res = max(res, r+1 - l)
        return res

            
