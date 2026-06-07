class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl=sorted(list(s))
        tl=sorted(list(t))
        print(sl)
        print(tl)
        if sl==tl:
            return True
        else:
            return False