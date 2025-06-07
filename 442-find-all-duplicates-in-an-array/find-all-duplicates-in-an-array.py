class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i] and nums[i] not in ans:
                ans.append(nums[i])
            
        return ans
        