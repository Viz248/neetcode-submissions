class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1=Counter(s1)
        lens1, lens2 = len(s1), len(s2)

        if lens1>lens2:
            return False

        l,r=0,lens1-1
        l2=[]
        for x in range(lens1):
            l2.append(s2[x])
        freq2=Counter(l2)
        while r+1<len(s2):
            r+=1
            l2.append(s2[r])
            l2.pop(0)
            l+=1
            
            freq2=Counter(l2)
            if freq1==freq2:
                return True
        return False
