class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n=len(nums)



        left=0
        right=n-1
        ans=[]
        start, end=-1, -1
        
        while(left<=right):
            mid=int((left+right)/2)
            if(nums[mid]==target):
                start=mid
                right=mid-1
            elif(nums[mid]<target):
                left=mid+1
            else:
                right=mid-1

        ans.append(start)

        left=0
        right=n-1













        while(left<=right):
            mid=int((right+left)/2)
            if(nums[mid]==target):
                end=mid
                left=mid+1
            elif(nums[mid]>target):
                right=mid-1
            else:
                left=mid+1

        ans.append(end)

        return ans





        


