class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        diff=-1
        i=0
        j=1
        while 0<=i<j<n:
            for i in range(n):
                for j in range(i+1,n):
                    if nums[i]<nums[j] and diff<nums[j]-nums[i]:
                        diff=nums[j]-nums[i]
        return diff
        