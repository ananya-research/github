class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # for i in range(len(nums)):
        #     if (nums[i]=1 and nums[i+1]=0) or (nums[i]=1 and nums[i1]=0):

        n=len(nums)
        l=0
        r=0
        zeroes=0
        maxLen=0
        length=0

        for r in range(n):

            if nums[r]==0:
                zeroes+=1
            
            while zeroes>k:
                if nums[l]==0:
                    zeroes-=1
                l+=1

            length=r-l+1
            maxLen=max(maxLen, length)
        
        return maxLen
        
            

            
            
           
            





                
        