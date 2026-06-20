class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        flag=False
        while left<right: 
            while not s[left].isalnum() and left<right:
                left+=1
            while not s[right].isalnum() and left<right:
                right-=1
            sl=s[left].lower()
            sr=s[right].lower()
            print(sl, sr)
            if sl!=sr:
                if flag==True:
                    return False
                elif s.count(sl)%2!=0:
                    print(sl," count is ",s.count(sl))
                    s=s.replace(sl,"")
                elif s.count(sr)%2!=0:
                    print(sr," count is ",s.count(sr))
                    s=s.replace(sr,"")
                else:
                    s=s.replace(sl,"")
                print(s)
                left=-1
                right=len(s)
                flag=True
            left+=1
            right-=1
        return True