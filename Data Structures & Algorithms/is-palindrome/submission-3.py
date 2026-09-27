class Solution:
    def isPalindrome(self, s: str) -> bool:
        # testStr = ''
        # for ch in s:
        #     if ch.isalnum():
        #         testStr += ch.lower()
        # return testStr == testStr[::-1]

        left, right = 0, len(s)-1
        while left<right:

            #Getting left char
            while left < right and not s[left].isalnum():
                left+=1

            while left < right and not s[right].isalnum():
                right-=1

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True