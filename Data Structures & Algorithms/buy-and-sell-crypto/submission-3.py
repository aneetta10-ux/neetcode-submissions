class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        p=0
        # r=l+1
        for l in range(0,len(prices)):
            for r in range(l+1,len(prices)):
                if prices[r]-prices[l]>p:
                    p= prices[r]- prices[l]
        return p