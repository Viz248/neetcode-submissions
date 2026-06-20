class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(x for x in s if x.isalnum()).lower()
        right=0
        left=len(s)-1
        while right<left:
            if s[right]!=s[left]:
                return False
            right+=1
            left-=1
        return True