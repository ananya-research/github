class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        total=0
        digit_sum=0

        n=len(nums)

        for i in range(n):
            total+=nums[i]
            m=str(nums[i])
            for j in m:
                digit_sum+=int(j)

        return abs(total-digit_sum)

        