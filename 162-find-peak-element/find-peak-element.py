class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n=len(nums)
       
        l=0
        r=n-1

        while l<=r:
            mid=(l+r)//2
            if mid >0 and nums[mid]<nums[mid-1]:
                r=mid-1
            elif mid<n-1 and nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                return mid
            
        return 0





            
        
        