class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        mx=0

        while r<len(prices):
            print(prices[l],prices[r])
            if prices[l]>=prices[r]:
                l=r
                r+=1
            else:
                profit=prices[r]-prices[l]
                mx=max(mx,profit)
                r+=1
        return mx
