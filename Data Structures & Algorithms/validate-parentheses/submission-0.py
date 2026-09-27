class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')':'(','}':'{', ']':'['}
        stack=[]
        for br in s:
            if br in hashMap.keys():
                if stack and hashMap[br] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(br)
        
        if stack:
            return False
        return True
