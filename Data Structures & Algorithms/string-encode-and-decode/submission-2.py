class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            str_len = int(s[i:j])
            end_point = j + 1 + str_len
            actual_string = s[j + 1: end_point]
            res.append(actual_string)
            i = end_point

        return res
