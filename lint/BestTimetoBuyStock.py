__author__ = 'sridhar'

class Solution:
    def maxProfit(self, prices):
        # write your code here

        curr = prices[0]
        res = 0
        for i in range(prices.__len__()):
            if i < curr:
                curr = prices[i]
                res += i-curr
                curr = i

        return res


class Solution:

    def maxProfit(self, prices):
        if len(prices) <= 1: return 0
        low = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < low: low = prices[i]
            maxprofit =  prices[i] - low
        return maxprofit
print Solution().maxProfit([1,2])

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1: return 0
        low = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < low: low = prices[i]
            maxprofit = max(prices[i]-low,maxprofit)
        return maxprofit