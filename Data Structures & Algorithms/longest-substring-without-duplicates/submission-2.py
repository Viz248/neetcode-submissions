class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l=r=0
        mx=1
        d={}
        d[s[l]]=l
        while r<len(s)-1:
            nxtchar=s[r+1]
            if nxtchar in d:
                target=d[nxtchar]+1
                while l!=target:
                    d.pop(s[l])
                    l+=1
                d[s[l]]=l

            r+=1
            d[s[r]]=r
            mx=max(mx,r-l+1)
        return mx