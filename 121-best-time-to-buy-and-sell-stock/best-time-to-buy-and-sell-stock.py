class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    # left_ptr, profit = 0, 0
    # for right_ptr in range(1, len(prices)):
    #   if prices[left_ptr] < prices[right_ptr]:
    #     profit = max(profit, prices[right_ptr] - prices[left_ptr])
    #   else:
    #     left_ptr = right_ptr
    # return profit

    # min_price=float('inf')
    # max_profit=0

    # for price in prices:
    #     if price<min_price:
    #         min_price=price
    #     profit=price-min_price
    #     if profit>max_profit:
    #         max_profit=profit
    # return max_profit

            









    maxProfit=0
    minPrice=float('inf')

    for price in prices:
        if price<minPrice:
            minPrice=price
        profit=price-minPrice
        maxProfit=max(maxProfit, profit)
    
    return maxProfit

