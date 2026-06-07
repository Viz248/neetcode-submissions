class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(x for x in s if x.isalnum()).lower()
        sl=list(s)
        slr=sl[::-1]
        if sl==slr:
            return True
        else:
            return False