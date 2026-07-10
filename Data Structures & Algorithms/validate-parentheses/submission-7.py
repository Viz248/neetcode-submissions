class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={')':'(',']':'[','}':'{'}
        for a in s:
            if a in d:
                if stack and stack[-1]==d[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)
        return not stack