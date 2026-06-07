class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for s_ele, t_ele in zip(s, t):
            count[ord(s_ele) - ord("a")] += 1
            count[ord(t_ele) - ord("a")] -= 1

        for value in count:
            if value != 0:
                return False

        return True
