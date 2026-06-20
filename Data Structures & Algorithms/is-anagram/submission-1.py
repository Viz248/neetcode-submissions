class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl=Counter(s)
        tl=Counter(t)
        if sl==tl:
            return True
        else:
            return False