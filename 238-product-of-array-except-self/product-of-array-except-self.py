class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # n=len(nums)

        # prefix=[1]*n
        # postfix=[1]*n

        # for i in range(1,n):
        #     prefix[i]=prefix[i-1]*nums[i-1]
        # print(prefix)

        # for i in range(n-2,-1,-1):
        #     postfix[i]=postfix[i+1]*nums[i+1]
        # print(postfix)

        # product=[1]*n

        # for i in range(n):
        #     product[i]=prefix[i]*postfix[i]

        # return product
            




        n=len(nums)
        answer=[1]*n

        prefix=[1]*n
        postfix=[1]*n

        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        
        for i in range(n-2, -1, -1):
            postfix[i]*=postfix[i+1]*nums[i+1]
        
        print(prefix)
        print(postfix)

        for i in range(n):
            answer[i]=prefix[i]*postfix[i]

        return answer




















        # n=len(nums)

        # prefix=[1]*n
        # suffix=[1]*n

        # for i in range(1, n):

        #     prefix[i]=prefix[i-1]*nums[i-1]

        # for i in range(n-2, -1, -1):
        #     suffix[i]=suffix[i+1]*nums[i+1]

        # ans=[]

        # for i in range(n):
        #     ans.append(prefix[i]*suffix[i])

        # return ans


            
        