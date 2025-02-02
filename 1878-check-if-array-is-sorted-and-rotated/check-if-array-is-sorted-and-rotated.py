class Solution:
    def check(self, nums: List[int]) -> bool:
        
        nums2=nums[:]
        nums.sort()
        print(nums,nums2)

        n=len(nums)

        A=[0]*n

        for i in range(n):
            
            new=[]
            new=nums[i:]
            new+=nums[:i]
            print(new)
            if new==nums2:
                return True

        return False


            
