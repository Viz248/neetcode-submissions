class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        mx=0

        while r<len(prices):
            print("\nl=",l,"r=",r)
            print(prices[l],prices[r])
            if prices[l]>=prices[r]:
                print("l>r")
                l=r
                r+=1
            else:
                profit=prices[r]-prices[l]
                print("l<r")
                print("max=",mx,"profit=",profit)
                mx=max(mx,profit)
                print("new_max=",mx)
                r+=1
        return mx
