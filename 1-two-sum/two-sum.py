class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # seen={}
        # for i in range(len(nums)):
        #     diff=target-nums[i]
        #     if diff in seen:
        #         return [seen[diff], i]
        #     else:
        #         seen[nums[i]]=i
        
        # for i in range(len(nums)):
        #     diff=target-nums[i]
        #     if diff in nums:
        #         ind=nums.index(diff)
        #         if i!=ind:
        #             return [ind, i]


    
        n=len(nums)
        for i in range(n):
            diff=target-nums[i]
            if diff in nums:
                ind=nums.index(diff)
                if ind!=i:
                    return [ind, i]