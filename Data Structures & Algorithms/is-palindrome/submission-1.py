class Solution:
    def isPalindrome(self, s: str) -> bool:
        testStr = ''

        for ch in s:
            if ch.isalnum():
                testStr += ch.lower()
        return testStr == testStr[::-1]