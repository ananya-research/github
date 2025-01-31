class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n=len(nums)

        # for i in range(n):
        #     if sum(nums[:i])==sum(nums[i+1:]):
        #         return i

        # return -1

        left_sum=0

        right_sum=sum(nums[1:])

        if right_sum==left_sum:
                return 0

   
        
        
        for i in range(1,n):

            left_sum+=nums[i-1]
            right_sum-=nums[i]

            if right_sum==left_sum:
                return i

        return -1
            

