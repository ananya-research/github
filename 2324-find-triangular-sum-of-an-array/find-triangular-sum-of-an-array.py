class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        n=len(nums)

        def func(arr, l):
            if l==1:
                return arr[0]
            newNums=[]
            for i in range(l-1):
                newNums.append((arr[i]+arr[i+1])%10)
            return func(newNums, len(newNums))
        
        return func(nums, n)
        


        