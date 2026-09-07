class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        k =1
        maxP = 0
        while k < len(prices):
            p = prices[k]-prices[j]
            maxP=max(maxP,p)
            if prices[k] < prices[j]:
                j = k
            k=k+1
        return maxP
        