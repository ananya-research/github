class Solution:
    def totalMoney(self, n: int) -> int:

        total=0

        for i in range(n):
            # total+=i
            rem=i%7
            quo=i//7
            print(rem+1,quo)
            total+=rem+1+quo
        
        return total






        