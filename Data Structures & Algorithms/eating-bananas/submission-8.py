class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<=r:
            k=(l+r)//2

            hours=0            
            for a in piles:
                hours+=(a+k-1)//k
                if hours>h:
                    break
            if hours>h:
                l=k+1
            else:
                r=k-1
        return r+1