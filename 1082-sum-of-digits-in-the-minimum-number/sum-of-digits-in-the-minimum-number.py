class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:

        # m=min(nums)

        # w=str(m)

        # while len(w)>1:
        #     s=0
        #     for i in w:
        #         s+=int(i)
        #     w=str(s)

        # if int(w)%2==0:
        #     flag=1
        #     return flag
        
        # else:
        #     flag=0
        #     return flag



        m=min(nums)

        w=str(m)

        
        s=0
        for i in w:
            s+=int(i)
            

        if int(s)%2==0:
            flag=1
            return flag
        
        else:
            flag=0
            return flag
        
        