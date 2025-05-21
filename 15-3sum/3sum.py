class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # h={}
        # n=len(nums)

        # s=list()

        # for i, num in enumerate(nums):
        #     h[num]=i


        # for i in range(n):
        #     for j in range(n):
        #         if i!=j:
        #             desired= -nums[i]-nums[j]
        #             if desired in h and h[desired]!=i and h[desired]!=j:
        #                 # s.append(tuple(sorted([nums[i], nums[j], desired])))
        #                 s.append(tuple([nums[i], nums[j], desired]))

        # print(list(set(s)))

        # return s

        # summ=0
        # n=len(nums)
        # nums.sort()
        # ans=[]

        # for i in range(n):
        #     if nums[i]>0:
        #         break
        #     elif i>0 and nums[i]==nums[i-1]:
        #         continue
        #     lo=i+1
        #     hi=n-1
        #     while lo<hi:
        #         summ=nums[i]+nums[lo]+nums[hi]
        #         if summ==0:
        #             ans.append([nums[i],nums[lo],nums[hi]])
        #             lo+=1
        #             hi-=1

        #             while lo<hi and nums[lo]==nums[lo-1]:
        #                 lo+=1
        #             while lo<hi and nums[hi]==nums[hi+1]:
        #                 hi-=1
                
        #         elif summ>0:
        #             hi-=1
        #         else:
        #             lo+=1
            
        # return ans



        res=[]
        nums.sort()

        n=len(nums)

        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            
            l=i+1
            r=n-1

            while l<r:
                threeSum=a+nums[l]+nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
            

        return res
            


                





        

        