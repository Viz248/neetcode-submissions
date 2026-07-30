class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        lens1, lens2 = len(s1), len(s2)

        if lens1>lens2:
            return False

        l,r=0,lens1-1
        freq1=Counter(s1)
        freq2={c:0 for c in freq1}

        for i in range(r+1):
            if s2[i] in freq2:
                freq2[s2[i]]+=1
            print(freq2)
        if freq1==freq2:
                return True
        while r+1<len(s2):
            r+=1
            if s2[r] in freq2:
                freq2[s2[r]]+=1
                
            if s2[l] in freq2:
                freq2[s2[l]]-=1 

            l+=1
            print(freq1,freq2)
            if freq1==freq2:
                return True
        return False
