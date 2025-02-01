class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        n=len(nums)

        c=0

        for i in range(n-1):
            if nums[i]%2!=nums[i+1]%2:
                c+=1

        return c+1==n



        