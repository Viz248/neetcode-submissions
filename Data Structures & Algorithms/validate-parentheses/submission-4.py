class Solution:
    def isValid(self, s: str) -> bool:
        s=list(s)
        stack=[]
        for a in s:
            if a=='(' or a=='[' or a=='{':
                stack.append(a)
            if a==')' or a==']' or a=='}':
                if not stack:
                    return False
                x=stack.pop()
                if not ((a==')' and x=='(') or (a==']' and x=='[') or (a=='}' and x=='{')):
                    return False
        if stack:
            return False
        else:
            return True

