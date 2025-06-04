class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProf=0
        # for i in range(0, len(prices)-1):
        #     if prices[i+1]>prices[i]:
        #         profit=prices[i+1]-prices[i]
        #         maxProf+=profit
        
        # return maxProf

        # profit=0

        # for i in range(1,len(prices)):
        #     if prices[i]>prices[i-1]:
        #         profit+=prices[i]-prices[i-1]

        # return profit

        # lo=prices[0]
        # hi=prices[0]
        # profit=0
        # i=0
        # n=len(prices)

        # while i<n-1:

        #     while i<n-1 and prices[i]>=prices[i+1]:
        #         i+=1
        #     lo=prices[i]

        #     while i<n-1 and prices[i]<prices[i+1]:
        #         i+=1
        #     hi=prices[i]

        #     profit+=hi-lo
        # return profit


        profit = 0
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, take the profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit




