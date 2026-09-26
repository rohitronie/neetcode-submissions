class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for ele_s, ele_t in zip(s,t):
            count[ord(ele_s) - ord('a')] += 1
            count[ord(ele_t) - ord('a')] -= 1
        
        for i in range(26):
            if count[i] != 0:
                return False
        
        return True
