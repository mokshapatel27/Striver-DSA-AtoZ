#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/2022534958/

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         minp=float(inf)
#         maxprof=0

#         for price in prices:
#             if price<minp:
#                 minp=price
#             elif price-minp>maxprof:
#                 maxprof=price-minp
#         return maxprof
                

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        minp=prices[0]
        maxprof=0

        for i in range(1,len(prices)):
            if prices[i]<minp:
                minp=prices[i]

            elif prices[i]-minp>maxprof:
                maxprof=prices[i]-minp
        return maxprof
