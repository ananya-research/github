class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(None)

        

        def simulate(curr, dir_step, nums_tuple):
            nums_list=list(nums_tuple)
            n=len(nums_list)

            while 0<=curr<n:
                if(nums_list[curr]==0):
                    curr+=dir_step
                elif(nums_list[curr]>0):
                    nums_list[curr]-=1
                    dir_step=-dir_step
                    curr+=dir_step

            return all(x==0 for x in nums_list)

        valid_count=0

        for i in range(len(nums)):
            if(nums[i]==0):
                nums_tuple=tuple(nums)
                if simulate(i,1,nums_tuple):
                    valid_count+=1
                if simulate(i, -1, nums_tuple):
                    valid_count+=1

        return valid_count
                    
        

        

        
        
        