class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1=Counter(s1)
        lens1, lens2 = len(s1), len(s2)

        if lens1>lens2:
            return False

        l,r=0,lens1-1
        freq2=Counter(s2[:lens1])

        if freq1==freq2:
                return True
        while r+1<len(s2):
            r+=1
            freq2[s2[r]]+=1
            freq2[s2[l]]-=1 

            if not freq2[s2[l]]:
                del freq2[s2[l]]
            l+=1
            
            if freq1==freq2:
                return True
        return False
