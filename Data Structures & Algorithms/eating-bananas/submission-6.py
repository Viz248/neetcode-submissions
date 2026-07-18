class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx=max(piles)
        if len(piles)==h:
            return mx
        
        l,r=1,mx
        while l<=r:
            k=(l+r)//2

            hours=0            
            for a in piles:
                hours+=(a+k-1)//k
            if hours>h:
                l=k+1
            elif hours<=h:
                new_hours=hours
                r=k-1
        return r+1