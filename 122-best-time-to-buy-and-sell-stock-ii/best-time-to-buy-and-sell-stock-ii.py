class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProf=0
        # for i in range(0, len(prices)-1):
        #     if prices[i+1]>prices[i]:
        #         profit=prices[i+1]-prices[i]
        #         maxProf+=profit
        
        # return maxProf

        profit=0

        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]

        return profit
            

        

        