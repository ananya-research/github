from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)

        count=defaultdict(int)
        p=0
        good=0
        
        for i in range(0,n):
            p+=i
            good+=count[nums[i]-i]
            count[nums[i]-i]+=1
        
        print(p)


        

        return p-good

        