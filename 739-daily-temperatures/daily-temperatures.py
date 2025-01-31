class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n=len(temperatures)

        ans=[0]*n

        stack=[]


        # for i in range(n):

        #     while stack and temperatures[i]>stack[-1]:
        #         a=stack.pop()
        #         ans[temperatures.index(a)]=i-temperatures.index(a)


        #     stack.append(temperatures[i])

       
    

        # return ans

        for i, temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]]<temp:
                a=stack.pop()
                ans[a]=i-a


            stack.append(i)

        return ans
            
            
        